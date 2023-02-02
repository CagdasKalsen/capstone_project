from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from . models import Product
from . models import Category
from . models import Cart
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class AllProducts(TemplateView):
    template_name = 'allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allproducts'] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    template_name = 'productdetail.html'
    model = Product


class AddToCart(View):
    def get(self, request, product_id):
        print(product_id)
        cart = Cart.objects.get(pk=1)
        cart.products.add(product_id)
        return redirect('home')


class About(TemplateView):
    template_name = "about.html"


class MyCart(TemplateView):
    template_name = "mycart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(pk=1)
        context['cart'] = cart
        return context


class Signup(View):
    def get(self):
        form = UserCreationForm()
        context = {"form": form}
        return context

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            return redirect("signup")
