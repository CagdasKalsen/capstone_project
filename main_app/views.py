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
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class AllProducts(TemplateView):
    template_name = 'allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context['products'] = Product.objects.filter(
                title__icontains=title, user=self.request.user)
            context['header'] = f"Searching for {title}"
        else:
            context['product'] = Product.objects.filter(
                user=self.request.user)
            context['header'] = 'All Products'
        return context


class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'category', 'price', 'image', 'description']
    template_name = 'product_create.html'
    success_url = "/allproducts"


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


class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'category', 'image', 'price', 'description']
    template_name = "product_update.html"

    def get_success_url(self):
        return reverse('productdetail', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    model = Product
    template_name = "product_delete_confirmation.html"
    success_url = '/'


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
