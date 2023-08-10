from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import *
import json
from django.core.paginator import Paginator
from django.http import JsonResponse


class index(View):
    def get(self, request):
        context = {
            'user': request.user,
            'categories': Category.objects.all(),
            'products': Product.objects.all(),
        }
        return render(request, 'pages/index.html', context)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)       
            if 'images' in request.FILES:
                product.images = request.FILES['images']
            product.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Product created for {name}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

class QuickView(View):
    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        # Aquí puedes agregar cualquier lógica adicional para obtener los datos necesarios del producto
        
        # Devolver los datos del producto como una respuesta JSON
        data = {
            'name': product.name,
            'category': product.category.name,
            'price': product.price,
            'description': str(product.description),
            'images': product.images.url,
            'status': product.status,
            'in_stock': product.in_stock,
            'code': product.code,
            'sku': product.sku,

            # Agrega más campos según tus necesidades
        }
        
        return JsonResponse(data)


def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def shopcart(request):
    return render(request,'pages/shop-cart.html')

def checkout(request):
    return render(request,'pages/shop-checkout.html')

def store_grid(request):
    return render(request,'pages/store-grid.html')

def store_list(request):
    return render(request,'pages/store-list.html')

def shop_grid(request):
    products = Product.objects.all()
    return render(request,'pages/shop-grid.html', {'products': products})


class shop_single(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        context = {
            'product': product,
        }
        
        return render(request, 'pages/shop-single.html', context)

def dashboard(request):
    context = {
        'user': request.user,       
    }
    return render(request,'dashboard/index.html', context)

def order_list(request):
    return render(request,'dashboard/order-list.html')

def order_single(request):
    return render(request,'dashboard/order-single.html')

def vendor_list(request):
    return render(request,'dashboard/vendor-list.html')

def vendor_grid(request):
    return render(request,'dashboard/vendor-grid.html')

def reviews(request):
    return render(request,'dashboard/reviews.html')

def customers(request):
    return render(request,'dashboard/customers.html')


def products(request):
    paginator = Paginator(Product.objects.all(), 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    total_pages = paginator.num_pages
    
    return render(request, 'dashboard/products.html', {'products': products, 'total_pages': total_pages})

def categories(request):
    paginator = Paginator(Category.objects.all(), 8)
    page = request.GET.get('page')
    categories = paginator.get_page(page)
    total_pages = paginator.num_pages
    return render(request,'dashboard/categories.html', {'categories': categories,'total_pages': paginator.num_pages})

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}")
                return redirect('index')  # redirige al usuario a la página de inicio
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrecta')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecta')
    else:
        form = AuthenticationForm()
    return render(request, '../templates/user/signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

class RegisterView(View):
    
    form_class = RegisterForm
    template_name = 'user/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if 'image' in request.FILES:
                user.image = request.FILES['image']
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')
        
        return render(request, self.template_name, {'form': form})
        
class create_category(View):
    form_class = CategoryForm
    initial = {'key': 'value'}
    template_name = '../templates/dashboard/add-category.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'categories': categories})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            if 'image' in request.FILES:
                category.image = request.FILES['image']
            category.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Category created for {name}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

class create_product(View):
    form_class = ProductForm
    initial = {'key': 'value'}
    template_name = '../templates/dashboard/add-product.html'
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'categories': categories})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = form.save(commit=False)       
            if 'images' in request.FILES:
                product.images = request.FILES['images']
            product.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Product created for {name}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})

class edit_product(View):
    form_class = ProductForm
    initial = {'key': 'value'}
    template_name = '../templates/dashboard/edit-product.html' 
    def get(self, request, *args, **kwargs):
        #show value of fields
        product = Product.objects.get(id=kwargs['pk'])
        form = self.form_class(instance=product)
        return render(request, self.template_name, {'form': form, 'product': product})

    def post(self, request, *args, **kwargs):
        #replace value of fields
        product = Product.objects.get(id=kwargs['pk'])
        form = self.form_class(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            if 'images' in request.FILES:
                product.images = request.FILES['images']
            product.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Product edited for {name}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

class delete_product(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product.delete()
        return redirect(to='/')

class ProductListView(View):
    template_name = 'dashboard/products.html'
    paginate_by = 8
    
    def get(self, request, *args, **kwargs):
        all_products = Product.objects.all()
        paginator = Paginator(all_products, self.paginate_by)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        
        context = {
            'products': products,
            'total_pages': paginator.num_pages
        }
        
        return render(request, self.template_name, context)

class CartView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products
        }     
        return render(request, '../templates/pages/shop-cart.html', context)


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
            self.cart = self.session['cart']
        else:
            self.cart = cart
    def add(self, product):
        id = str(product.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                'product_id': product.id,
                'name': product.name,
                'quantity': 1,
                'price': product.price,
                'image': product.images.url,
            }
        else:
            self.cart[id]['quantity'] += 1
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    def remove(self, product):
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.save()
    def decrement(self, product):
        id = str(product.id)
        if id in self.cart:
            if self.cart[id]['quantity'] > 1:
                self.cart[id]['quantity'] -= 1
                self.save()
            else:
                self.remove(product)
    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

def add_product(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect(to='index')

def remove_product(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect(to='index')

def decrement_product(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.decrement(product)
    return redirect(to='index')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect(to='index')

