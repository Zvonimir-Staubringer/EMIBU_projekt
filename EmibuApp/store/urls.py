from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name="products"),
    path('contact', views.contact_view, name="contact"),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('products/<int:id>', views.detail_view, name="detail"),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('new_order/', views.new_order, name='new_order'),
    path('payment/', views.payment, name="payment"),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_list, name='orders'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('products/by_name/<str:name>/', views.detail_view_name, name='detail_name'),
    path('project/<int:id>/complete', views.project_complete, name='project_complete'),
]