from math import ceil
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact, Product, Order, UpdateOrder
import json
from django.contrib import messages

# Create your views here.


def index(request):
    all_prods = []
    categorys_values = Product.objects.values('category')
    categorys = {item['category'] for item in categorys_values}
    for category in categorys:
        prod = Product.objects.filter(category=category)
        n = len(prod)
        no_slides = n // 4 + ceil((n/4) - (n//4))
        all_prods.append([prod, range(1, no_slides), no_slides])
    params = {"all_products": all_prods}
    return render(request, "buybest/index.html", params)


def SearchMatch(search, item):
    if search.lower() in item.product_name.lower() or search.lower() in item.category.lower():
        return True
    else:
        return False


def search(request):
    search = request.GET.get('search')
    all_prods = []
    categorys_values = Product.objects.values('category')
    categorys = {item['category'] for item in categorys_values}
    for category in categorys:
        prods = Product.objects.filter(category=category)
        prod = [item for item in prods if SearchMatch(search, item)]
        n = len(prod)
        no_slides = n // 4 + ceil((n/4) - (n//4))
        if len(prod) != 0 and len(search) < 5 and no_slides != 0:
            all_prods.append([prod, range(1, no_slides), no_slides])
        else:
            n = len(prods)
            # Empty courisers Remove them
            no_slides = n // 4 + ceil((n / 4) - (n // 4))
            all_prods.append([prods, range(1, no_slides), no_slides])
    if len(prod) == 0:
        messages.warning(request, "We're sorry. We cannot find any matches for your search term.")
    params = {"all_products": all_prods}
    return render(request, "buybest/index.html", params)


def about(request):
    return render(request, 'buybest/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        phone = request.POST.get('phone', default=0)
        email = request.POST.get('email', '')
        message = request.POST.get('message', "")
        contact_info = Contact(name=name, phone=phone,
                               email=email, message=message)
        contact_info.save()
        messages.success(
            request, 'Thanks for contacting us. We will get back to you soon...')
    return render(request, 'buybest/contact.html')


def products(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "buybest/view.html", {"product": product[0]})


def Tracker(request):
    if request.method == 'POST':
        orderid = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(id=orderid, email=email)
            if len(order) > 0:
                update = UpdateOrder.objects.filter(order_id=orderid)
                updates = []
                for i in update:
                    updates.append({'text': i.order_status, 'time': i.date})
                    response = json.dumps(
                        {'status': 'success', 'updates': updates, 'items': order[0].item_json}, default=str)
                return HttpResponse(response)
            else:
                noitem = json.dumps({'status': 'noitems'}, default=str)
                return HttpResponse(noitem)
        except Exception as e:
            error = json.dumps({'status': 'error'}, default=str)
            return HttpResponse(error)
    return render(request, 'buybest/tracker.html')


def CheckOut(request):
    if request.method == "POST":
        item_json = request.POST.get('item_json', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(item_json=item_json, name=name, email=email, phone=phone, address=address, city=city,
                      state=state, zip_code=zip_code)
        order.save()
        uid = order.id
        update = UpdateOrder(
            order_id=order.id, order_status="Your order has been placed")
        update.save()
        return redirect(f'/thanksforshoppingwithus/{uid}')

    return render(request, 'buybest/checkout.html')


def ordered(request, orderid):
    op = Order.objects.filter(id=orderid)
    if len(op) > 0:
        return render(request, 'buybest/ordered.html', {'id': orderid})
    else:
        return redirect('/')
