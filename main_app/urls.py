from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('allproducts', views.AllProducts.as_view(), name='allproducts'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='productdetail'),
    path('addtocart/<int:product_id>/',
         views.AddToCart.as_view(), name='addtocart'),
    path('mycart', views.MyCart.as_view(), name='mycart'),

    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('products/new/', views.ProductCreate.as_view(), name="product_create")
]
