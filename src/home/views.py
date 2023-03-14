from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    ihas = Iha.objects.all()
    return render(request, "index.html", {'ihas':ihas})

def customer_signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        city = request.POST['city']

        if password1 != password2:
            return redirect("/customer_signup")

        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
        user.save()
        try:
            location = Location.objects.get(city=city.lower())
        except:
            location = None
        if location is not None:
            customer = Customer(user=user, phone=phone, location=location, type="Customer")
        else:
            location = Location(city=city.lower())
            location.save()
            location = Location.objects.get(city=city.lower())
            customer = Customer(user=user, phone=phone, location=location, type="Customer")
        customer.save()
        alert = True
        return render(request, "customer_signup.html", {'alert':alert})
    return render(request, "customer_signup.html")

def customer_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None and user.is_authenticated:
                user1 = Customer.objects.get(user=user)
                if user1.type == "Customer":
                    login(request, user)
                    return redirect("/customer_homepage")
            else:
                alert = True
                return render(request, "customer_login.html", {'alert':alert})
    return render(request, "customer_login.html")

def iha_dealer_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return redirect('/iha_dealer_signup')

        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
        user.save()
        try:
            location = Location.objects.get(city = city.lower())
        except:
            location = None
        if location is not None:
            iha_dealer = IhaDealer(iha_dealer=user, phone=phone, location=location, type="Iha Dealer")
        else:
            location = Location(city = city.lower())
            location.save()
            location = Location.objects.get(city = city.lower())
            iha_dealer = IhaDealer(iha_dealer = user, phone=phone, location=location, type="Iha Dealer")
        iha_dealer.save()
        return render(request, "iha_dealer_login.html")
    return render(request, "iha_dealer_signup.html")

def iha_dealer_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                try:
                    user1 = IhaDealer.objects.get(iha_dealer=user)
                except ObjectDoesNotExist:
                    # Handle the DoesNotExist exception here
                    alert = True
                    return render(request, "iha_dealer_login.html", {"alert": alert})
                if user1.type == "Iha Dealer":
                    login(request, user)
                    return redirect("/all_ihas")
                else:
                    alert = True
                    return render(request, "iha_dealer_login.html", {"alert": alert})
    return render(request, "iha_dealer_login.html")

def signout(request):
    logout(request)
    return redirect('/')

def add_iha(request):
    if request.method == "POST":
        iha_name = request.POST['iha_name']
        city = request.POST['city']
        image = request.FILES['image']
        rent = request.POST['rent']
        operational_altitude = request.POST['operational_altitude']
        max_altitude = request.POST['max_altitude']
        max_flight_time = request.POST['max_flight_time']
        payload_capacity = request.POST['payload_capacity']
        communication_range = request.POST['communication_range']
        fuel_capacity = request.POST['fuel_capacity']
        cruise_speed = request.POST['cruise_speed']
        max_speed = request.POST['max_speed']
        max_takeoff_weight = request.POST['max_takeoff_weight']
        height = request.POST['height']
        wingspan = request.POST['wingspan']
        lenght = request.POST['lenght']
        iha_dealer = IhaDealer.objects.get(iha_dealer=request.user)
        
        try:
            location = Location.objects.get(city=city)
        except Location.DoesNotExist:
            location = Location(city=city)
            location.save()
        
        iha = Iha(name=iha_name, iha_dealer=iha_dealer, location=location, image=image, rent=rent, operational_altitude=operational_altitude, max_altitude=max_altitude, max_flight_time=max_flight_time, payload_capacity=payload_capacity, communication_range=communication_range, fuel_capacity=fuel_capacity, cruise_speed=cruise_speed, max_speed=max_speed, max_takeoff_weight=max_takeoff_weight, height=height, wingspan=wingspan, lenght=lenght)
        iha.save()
        alert = True
        return render(request, "add_iha.html", {'alert':alert})
    return render(request, "add_iha.html")

def all_ihas(request):
    dealer = IhaDealer.objects.filter(iha_dealer=request.user).first()
    ihas = Iha.objects.filter(iha_dealer=dealer)
    return render(request, "all_ihas.html", {'ihas':ihas})

def edit_iha(request, myid):
    iha = Iha.objects.filter(id=myid)[0]
    if request.method == "POST":
        iha_name = request.POST['iha_name']
        city = request.POST['city']
        capacity = request.POST['capacity']
        rent = request.POST['rent']

        iha.name = iha_name
        iha.city = city
        iha.capacity = capacity
        iha.rent = rent
        iha.save()

        try:
            image = request.FILES['image']
            iha.image = image
            iha.save()
        except:
            pass
        alert = True
        return render(request, "edit_iha.html", {'alert':alert})
    return render(request, "edit_iha.html", {'iha':iha})

def delete_iha(request, myid):
    if not request.user.is_authenticated:
        return redirect("/iha_dealer_login")
    iha = Iha.objects.filter(id=myid)
    iha.delete()
    return redirect("/all_ihas")

def customer_homepage(request):
    return render(request, "customer_homepage.html")

def search_results(request):
    city = request.POST['city']
    city = city.lower()
    vehicles_list = []
    location = Location.objects.filter(city = city)
    for a in location:
        ihas = Iha.objects.filter(location=a)
        for iha in ihas:
            if iha.is_available == True:
                vehicle_dictionary = {'name':iha.name, 'id':iha.id, 'image':iha.image.url, 'city':iha.location.city, 'rent':iha.rent, 'operational_altitude':iha.operational_altitude, 'max_altitude':iha.max_altitude, 'max_flight_time':iha.max_flight_time, 'payload_capacity':iha.payload_capacity, 'communication_range':iha.communication_range, 'fuel_capacity':iha.fuel_capacity, 'cruise_speed':iha.cruise_speed, 'max_speed':iha.max_speed, 'max_takeoff_weight':iha.max_takeoff_weight, 'height':iha.height, 'wingspan':iha.wingspan, 'lenght':iha.lenght}
                vehicles_list.append(vehicle_dictionary)
    request.session['vehicles_list'] = vehicles_list
    return render(request, "search_results.html")

def iha_rent(request):
    id = request.POST['id']
    iha = Iha.objects.get(id=id)
    cost_per_day = int(iha.rent)
    return render(request, 'iha_rent.html', {'iha':iha, 'cost_per_day':cost_per_day})

def order_details(request):
    iha_id = request.POST['id']
    username = request.user
    user = User.objects.get(username=username)
    days = request.POST['days']
    iha = Iha.objects.get(id=iha_id)
    if iha.is_available:
        iha_dealer = iha.iha_dealer
        rent = (int(iha.rent))*(int(days))
        iha_dealer.earnings += rent
        iha_dealer.save()
        try:
            order = Order(iha=iha, iha_dealer=iha_dealer, user=user, rent=rent, days=days,)
            order.save()
        except:
            order = Order.objects.get(iha=iha, iha_dealer=iha_dealer, user=user, rent=rent, days=days)
        iha.is_available = False
        iha.save()
        return render(request, "order_details.html", {'order':order})
    return render(request, "order_details.html")

def past_orders(request):
    all_orders = []
    user = User.objects.get(username=request.user)
    try:
        orders = Order.objects.filter(user=user)
    except:
        orders = None
    if orders is not None:
        for order in orders:
            if order.is_complete == False:
                order_dictionary = {'id':order.id, 'rent':order.rent, 'iha':order.iha, 'days':order.days, 'iha_dealer':order.iha_dealer}
                all_orders.append(order_dictionary)
    return render(request, "past_orders.html", {'all_orders':all_orders})

def delete_order(request, myid):
    order = Order.objects.filter(id=myid)
    order.delete()
    return redirect("/past_orders")

def all_orders(request):
    username = request.user
    user = User.objects.get(username=username)
    iha_dealer = IhaDealer.objects.get(iha_dealer=user)
    orders = Order.objects.filter(iha_dealer=iha_dealer)
    all_orders = []
    for order in orders:
        if order.is_complete == False:
            all_orders.append(order)
    return render(request, "all_orders.html", {'all_orders':all_orders})

def complete_order(request):
    order_id = request.POST['id']
    order = Order.objects.get(id=order_id)
    iha = order.iha
    order.is_complete = True
    order.save()
    iha.is_available = True
    iha.save()
    return HttpResponseRedirect('/all_orders/')

def earnings(request):
    username = request.user
    user = User.objects.get(username=username)
    iha_dealer = IhaDealer.objects.get(iha_dealer=user)
    orders = Order.objects.filter(iha_dealer=iha_dealer)
    all_orders = []
    for order in orders:
        all_orders.append(order)
    return render(request, "earnings.html", {'amount':iha_dealer.earnings, 'all_orders':all_orders})
   
