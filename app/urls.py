from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import LoginView,RegisterView,create_category  # Import the view here

urlpatterns =[
    path('',views.index.as_view(),name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('shopcart/',views.shopcart,name='shopcart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store_grid/',views.store_grid,name='store_grid'),
    path('store_list/',views.store_list,name='store_list'),
    path('shop_grid/',views.shop_grid,name='shop_grid'),
    path('shop_single/<int:product_id>/', views.shop_single.as_view(), name='shop_single'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.LoginView, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('products/',views.products,name='products'),
    path('categories/',views.categories,name='categories'),
    path('create_category/',create_category.as_view(),name='create_category'),
    path('create_product/',views.create_product.as_view(),name='create_product'),
    path('edit_product/<int:pk>/',views.edit_product.as_view(),name='edit_product'),
    path('delete_product/<int:pk>/',views.delete_product.as_view(),name='delete_product'),
    path('order_list/',views.order_list,name='order_list'),
    path('order_single/',views.order_single,name='order_single'),
    path('vendor_list/',views.vendor_list,name='vendor_list'),
    path('vendor_grid/',views.vendor_grid,name='vendor_grid'),
    path('customers/',views.customers,name='customers'),
    path('reviews/',views.reviews,name='reviews'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('quick_view/<int:product_id>/', views.QuickView.as_view(), name='quick-view'),


    path('add_to_cart/<int:product_id>/', views.add_product, name='Add'),
    path('remove/<int:product_id>/', views.remove_product, name='Remove'),
    path('decreament_from_cart/<int:product_id>/', views.decrement_product, name='decrement_product'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),


    path('cart/', views.CartView.as_view(), name='cart'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  