from django.shortcuts import render,redirect
from .models import *
from .forms import ProductForm
from django.contrib import messages
from django.http import JsonResponse
import datetime 
# from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        cartItems= order.get_total_quantity
    else:
        items=[]
        order={'get_total_quantity':0,
               'get_chart_total': 0}
        cartItems= order['get_total_quantity']

    items=Product.objects.all()
    context={'form': items,
            'cartItems':cartItems

            }
    return render(request, 'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer,complete=False)

        items= order.orderitem_set.all()
        cartItems= order.get_total_quantity

    else:
        items=[]
        order={'get_total_quantity':0,
               'get_chart_total': 0}
        cartItems= order['get_total_quantity']

    context={'items': items,
             'order': order,
             'cartItems': cartItems  
            }
    return render(request, 'store/cart.html',context)

def checkout(request):

    if request.user.is_authenticated:
        customer= request.user.customer
        order,created= Order.objects.get_or_create(customer=customer,complete=False)

        items= order.orderitem_set.all()
        cartItems= order.get_total_quantity


    else:
        items=[]
        order={'get_total_quantity':0,
               'get_chart_total': 0}
        cartItems= order['get_total_quantity']

    context={'items': items,
             'order': order,
             'cartItems': cartItems   
            }
    return render(request, 'store/checkout.html',context)


def image(request):
    form= Customer.objects.all()
    context={
        'data' : form
    }
    return render(request,'store/check.html',context)

def addproduct(request):
    form=ProductForm()

    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Product Is added Successfully")
            return redirect('/')


    context={
        'form':form
    }
    return render(request,'store/addproduct.html',context)


def updateItem(request):
    data= json.loads(request.body)
    productId= data['productId']
    action=data['action']
    
    customer =request.user.customer
    product= Product.objects.get(id= productId)
    order,created= Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created= OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse("Hello from cart added", safe=False)


def ProcessOrder(request):

    transaction_id = datetime.datetime.now().timestamp()
    data= json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created= Order.objects.get_or_create(customer=customer, complete=False)

        total=float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_chart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order= order,
            address= data['shipping']['address'],
            city= data['shipping']['city'],
            state= data['shipping']['state'],
            zipcode= data['shipping']['zipcode'],
        )
        print("Transaction Completed")

    else:
        print("user not logged in...")


    return JsonResponse("Payment complete", safe=False)