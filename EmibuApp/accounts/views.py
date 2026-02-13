from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from store.models import Customer, Order, CustomProject
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        if form.is_valid():
            user = form.save()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
        
            Customer.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            login(request, user)
            return redirect("home_page")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def dashboard(request):
    user = request.user
    customer = user.customer
    orders = Order.objects.filter(customerID=customer).order_by("-order_date")

    for index, order in enumerate(reversed(orders), start=1):
        order.customer_order_number = index

    projects = CustomProject.objects.filter(customerID=customer).order_by("-request_date")
    
    context = {
        'user': user,
        'orders': orders,
        'projects' : projects,
    }

    return render(request, 'accounts/dashboard.html', context)
