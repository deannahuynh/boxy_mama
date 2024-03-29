from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "main/landingPage.html")

def home(request):
    return render(request,"main/homePage.html")

def halloween(request):
    return render(request, "main/halloween.html")

def everyday(request):
    return render(request, "main/everyday.html")

def order_page(request):
    return render(request, "main/orderPage.html")

def order(request):
    if request.method == 'POST':
        errors = Order.objects.basic_validator(request.POST)
        errors1 = Address.objects.basic_validator(request.POST)
        form = request.POST
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
        if len(errors1) > 0:
            for key, value in errors1.items():
                messages.error(request,value)
                # print(errors1)
                return redirect ('/order-page')
        form = request.POST
        new_address= Address.objects.create( 
            street_address=form['street_address'], 
            address_2= form['street_address2'], 
            city=form['city'], 
            state=form['state'], 
            zip_code=form['zip'], 
            country=form['country']
            )
        new_order= Order.objects.create(
            box_theme = form["box_theme"],
            first_name = form['first_name'], 
            last_name = form['last_name'], 
            email = form['email'], 
            note = form['note'], 
            address = new_address
            )
        order_id = str(new_order.id)
        return redirect('/shopping-cart/' + order_id)
    

def edit_order(request, order_id):
    order = Order.objects.filter(id=order_id)
    if order:
        order_to_edit= Order.objects.get(id=order_id)
        print("edit this order", order_to_edit)
        # print("address by id", order_to_edit["address_id"])
        address_to_edit= Address.objects.get(id=order_to_edit.address_id)
        context = {
            "order_to_edit" : order_to_edit,
            "address_to_edit" : address_to_edit,
        }
        return render(request,"main/editPage.html", context)
    else: 
        return redirect('/')

def update(request, order_id):
    order = Order.objects.filter(id=order_id)
    if order and request.method == 'POST':
        errors = Order.objects.basic_validator(request.POST)
        errors1 = Address.objects.basic_validator(request.POST)
        form = request.POST
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
        if len(errors1) > 0:
            for key, value in errors1.items():
                messages.error(request,value)
                print(errors1)
                return redirect ('/order/edit/' + order_id)
        order_to_update= Order.objects.get(id=order_id)
        address_to_update= Address.objects.get(id=order_to_update.address_id)
        address_to_update.street_address = request.POST['street_address']
        address_to_update.address_2 = request.POST['street_address2']
        address_to_update.city= request.POST['city']
        address_to_update.state= request.POST['state']
        address_to_update.country= request.POST['country']
        address_to_update.save()
        order_to_update.box_theme = request.POST['box_theme']
        order_to_update.first_name = request.POST['first_name']
        order_to_update.last_name = request.POST['last_name']
        order_to_update.email = request.POST['email']
        order_to_update.note = request.POST['note']
        order_to_update.address = address_to_update
        order_to_update.save()
        return redirect('/shopping-cart/' + order_id)
    else:
        return redirect('/')

def cart(request, order_id):
    order = Order.objects.filter(id=order_id)
    if order:
        order_in_cart = Order.objects.get(id=order_id)
        rec_address= Address.objects.get(id=order_in_cart.address_id)
        context = {
            "order" : order_in_cart,
            "address" : rec_address,

        }
        return render(request, "main/cart.html", context)
    else: 
        return redirect('/')
