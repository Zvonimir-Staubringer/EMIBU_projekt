from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Product, CustomProject, Order, OrderLine, OrderProduct
from django.db.models import Count, Q
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .cart import Cart
# Create your views here.



def home(request):
    context = {
    }
    return render(request, 'store/homepage.html', context)

def products(request):
    products = Product.objects.filter(availability=True).order_by("type", "name") 

    product_types = Product.objects.filter(availability=True).values("type").annotate(count=Count("id"))

    grouped_products = {}
    for product in products:
        if product.type not in grouped_products:
            grouped_products[product.type] = []
        grouped_products[product.type].append(product)

    return render(
        request,
        "store/products.html",
        {
            "product_types": grouped_products,
            "nav_product_types": product_types,
        },
    )

@login_required
def contact_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        request_text  = request.POST.get("request_text")

        if title and request_text:
            CustomProject.objects.create(
                title=title,
                request_text=request_text,
                customerID=request.user.customer
            )
            messages.success(request, "Your request has been sent successfully!")
        else:
            messages.error(request, "Please fill in all fields!")

    return render(request, "store/contact.html")

def cart_detail(request):
    cart = Cart(request)
    is_empty = cart.__len__() == 0
    context = {
        'cart': cart,
        'is_empty': is_empty,
    }
    return render(request, 'store/cart_detail.html', context)

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, override_quantity=False)
    return redirect('cart_detail')

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, override_quantity=True)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

def new_order(request):
    cart = Cart(request)
    if request.method == "POST":
        if cart.__len__() > 0:
            return redirect('checkout')
        else:
            messages.error(request, "Your cart is empty!")
            return redirect('cart_detail')

def checkout(request):
    cart = Cart(request)
    context = { 'cart': cart, }
    return render(request, 'store/checkout.html', context)

def payment(request):
    cart = Cart(request)
    if cart.__len__() == 0:
        messages.error(request, "Something went wrong!")
        return redirect('cart_detail')
    
    if request.method == "POST":
        
        if request.user.is_authenticated:
            customer = request.user.customer
        else:
            customer = None
        card_number = request.POST.get('cardnumber')
        expiration_month = request.POST.get('expirationmonth')
        expiration_year = request.POST.get('expirationyear')
        CVV_number = request.POST.get('CVVnumber')
        delivery_address = request.POST.get('address')
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')

        # Validate form fields
        if not (delivery_address and first and last and email and card_number and expiration_month and expiration_year and CVV_number and first):
            messages.error(request, "All fields are required.")
            return redirect('checkout')

        try:
            expiration_month = int(expiration_month)
            expiration_year = int(expiration_year)
        except ValueError:
            messages.error(request, "Invalid expiration date.")
            return redirect('checkout')

        valid_year = False
        if expiration_year >= timezone.now().year:
            if expiration_month >= timezone.now().month:
                valid_year = True

        context = {}

        if (len(card_number) == 16) and valid_year and len(CVV_number) == 3:
            order = Order.objects.create(customerID=customer, total_price=cart.get_total_price())
        
            for item in cart:
                product = item['product']
                order_product = OrderProduct.objects.create(
                    type=product.type,
                    name=product.name,
                    price=product.price,
                    image=product.image,
                    description=product.description
                )
                OrderLine.objects.create(orderID=order, productID=order_product, quantity=item['quantity'])
                
            order_lines = order.orderline_set.all()
            for order_line in order_lines:
                order_line.total_price = order_line.productID.price * order_line.quantity
                order_line.save()
                order.processed = True
                order.delivery_address = delivery_address
                order.first_name = first
                order.last_name = last
                order.email = email
                order.save()
                messages.success(request, "Order has been processed!")

            context = {
                'order': order,
                'order_lines': order_lines,
            }
            cart.clear()
            return render(request, 'store/payment.html', context)
        else:
            messages.error(request, "Invalid card information! Please try again.")
            return redirect('checkout')

def detail_view(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
    }
    return render(request, 'store/detail.html', context)

@login_required
def order_list(request):
    if request.user.is_superuser:
        query_orders = request.GET.get('qo')
        if query_orders:
            orders = Order.objects.filter(
                Q(customerID__first_name__icontains=query_orders) | 
                Q(customerID__last_name__icontains=query_orders)
            ).order_by('-order_date')
        else:
            orders = Order.objects.all().order_by('-order_date')
        
        query_projects = request.GET.get('qp')
        if query_projects:
            projects = CustomProject.objects.filter(
                Q(customerID__first_name__icontains=query_projects) | 
                Q(customerID__last_name__icontains=query_projects)
            ).order_by('completed', '-request_date')
        else:
            projects = CustomProject.objects.all().order_by('completed', '-request_date')
        
        context = {
            'orders': orders,
            'projects': projects,
            'query_orders': query_orders,
            'query_projects': query_projects,
        }
        return render(request, 'store/order_list.html', context)
    else:
        return redirect('home_page')
    
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_lines = order.orderline_set.all()
    context = {
        'order': order,
        'order_lines': order_lines,
    }
    return render(request, 'store/order_detail.html', context)

@login_required
def project_complete(request, id):
    project = get_object_or_404(CustomProject, pk=id)
    project.completed = True
    project.save()

    return redirect('orders')

def detail_view_name(request, name):
    product = get_object_or_404(Product, name=name)
    product_id = product.id
    return redirect('detail', product_id)
