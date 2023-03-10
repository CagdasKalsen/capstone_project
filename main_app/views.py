from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from . models import Product, Customers
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     title = self.request.GET.get("title")
    #     if title != None:
    #         context['products'] = Product.objects.filter(
    #             title__icontains=title, user=self.request.user)
    #         context['header'] = f"Searching for {title}"
    #     else:
    #         context['product'] = Product.objects.filter(
    #             user=self.request.user)
    #         context['header'] = 'All Products'
    #     return context


class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'category', 'price', 'image', 'description']
    template_name = 'product_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('productdetail', kwargs={'pk': self.object.pk})


class ProductDetail(DetailView):
    template_name = 'productdetail.html'
    model = Product


class AddToCart(View):
    def get(self, request, product_id):
        cart = Cart.objects.get(pk=4)
        cart.products.add(product_id)
        return redirect('mycart')
    # def get(self, request, product_id):
    #     product = Product.objects.get(id=product_id)
    #     cart = Cart.objects.get(customer=request.user.pk)
    #     cart.products.add(product)
    #     return redirect('mycart')


class About(TemplateView):
    template_name = "about.html"


class MyCart(TemplateView):
    template_name = "mycart.html"
    # model = Customers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(pk=4)
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


class ItemDelete(DeleteView):
    model = Cart
    template_name = "cart_update.html"
    success_url = 'mycart'


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
