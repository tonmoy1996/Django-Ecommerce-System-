from django.urls import path
from . import views 
urlpatterns=[

    path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('login', views.loginPage, name="login"),
	path('logout/', views.logoutPage, name="logout"),
	path('register/', views.registerPage, name="register"),
	path('checkout/', views.checkout, name="checkout"),
	path('create/',views.addproduct,name="createproduct"),
	path('update_item/',views.updateItem,name="update_item"),
	path('process_order/',views.ProcessOrder,name="process_order"),
	path('orders/', views.orderlist, name='order_list')



]