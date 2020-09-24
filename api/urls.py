from django.contrib import admin
from django.urls import path , include
from . import views
app_name='api'


urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/users/<int:id>', views.user, name='user_details'),
    path('api/add/', views.add_user.as_view(), name='add'),
    path('api/search', views.Search.as_view(), name='search'),
    path('api/product', views.Product.as_view(), name='product'),
    path('api/mouseclick', views.Mouse_Click.as_view(), name='mouseclick'),
    path('api/cart', views.Cart.as_view(), name='cart'),
    path('api/addtocart', views.Add_To_Cart.as_view(), name='addtocart'),
    path('api/deletefromthecart', views.Delete_From_The_Cart.as_view(), name='deletefromthecart'),
    path('api/checkout', views.Checkout.as_view(), name='checkout'),
]
