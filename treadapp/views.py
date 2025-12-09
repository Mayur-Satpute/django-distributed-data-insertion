from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Product, Order
import threading

# Create your views here.

users = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", "bob@example.com"),
    (3, "Charlie", "charlie@example.com"),
    (4, "David", "david@example.com"),
    (5, "Eve", "eve@example.com"),
    (6, "Frank", "frank@example.com"),
    (7, "Grace", "grace@example.com"),
    (8, "Alice", "alice@example.com"),
    (9, "Henry", "henry@example.com"),
    (10, "", "jane@example.com"),
]


products = [
    (1, "Laptop", 1000.00),
    (2, "Smartphone", 700.00),
    (3, "Headphones", 150.00),
    (4, "Monitor", 300.00),
    (5, "Keyboard", 50.00),
    (6, "Mouse", 30.00),
    (7, "Laptop", 1000.00),
    (8, "Smartwatch", 250.00),
    (9, "Gaming Chair", 500.00),
    (10, "Earbuds", -50.00),
]


orders = [
    (1, 1, 1, 2),
    (2, 2, 2, 1),
    (3, 3, 3, 5),
    (4, 4, 4, 1),
    (5, 5, 5, 3),
    (6, 6, 6, 4),
    (7, 7, 7, 2),
    (8, 8, 8, 0),
    (9, 9, 1, -1),
    (10, 10, 11, 2),
]

output={"users":[], "products":[], "orders":[]}



def adduser(data):
    id, name, email = data
    if name and email:
        User.objects.using("usersdb").create(id=id, name=name, email=email)
        output["users"].append((id,"User Added"))
    else:
        output["users"].append((id,"Invalid Name"))
    

def addproduct(data):
    id, name, price = data
    if price >= 0:
        Product.objects.using("productsdb").create(id=id, name=name, price=price)
        output["products"].append((id, "Product Added"))
    else:
        output["products"].append((id, "Invalid Price!!"))

def addorder(data):
    id, user, product, quantity = data
    if quantity > 0:
        Order.objects.using("ordersdb").create(id=id, user_id=user, product_id=product, quantity=quantity)
        output["orders"].append((id, "Order Added"))
    else:
        output["orders"].append((id, "Invalid quantity"))



def run_all(request):

    output["users"] = []
    output["products"] = []
    output["orders"] = []

    # Clear old DB records so no duplicate primary key error
    User.objects.using("usersdb").all().delete()
    Product.objects.using("productsdb").all().delete()
    Order.objects.using("ordersdb").all().delete()
    threads = []

    #users
    for u in users:
        t = threading.Thread(target=adduser, args=(u,))
        threads.append(t)


    #products
    for p in products:
        t = threading.Thread(target=addproduct, args=(p,))
        threads.append(t)

    #orders
    for o in orders:
        t = threading.Thread(target=addorder, args=(o,))
        threads.append(t)

    # Start all threads here
    for t in threads:
        t.start()

    # Wait for threads to finish their work!!
    for t in threads:
        t.join()

    return HttpResponse(
        f"<h2>Insertion Completed</h2>"
        f"<br><br>Users: {output['users']}<br><br>"
        f"Products: {output['products']}<br><br>"
        f"Orders: {output['orders']}"
    )



