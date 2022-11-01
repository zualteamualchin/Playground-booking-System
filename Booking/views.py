from asyncio.windows_events import NULL
import email
from email.errors import MessageError
from sqlite3 import Date
from unicodedata import name
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Booking.decorators import unauthenticated_user
from .models import Customer,Scheduler,Booked,Location,Manager
from Booking import models
from .forms import BookedForm,CustomerForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

from django.contrib import messages
from json import dumps
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
# Create your views here.

def index(request):
    if request.user.is_authenticated: 
        return render(request, 'accounts/C_index.html')
    else:
        return render(request, 'index.html')

def indoor(request):
    if request.user.is_authenticated: 
        return render(request, 'accounts/C_indoor.html')
    else:
        return render(request, 'indoor.html')

def outdoor(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/C_outdoor.html')
    else:
        return render(request, 'outdoor.html')

def location(request):
    
    locs = Location.objects.all()
    locate = []
    for i in locs:
        locate.append(i.place+ ", " +i.local+ ", "+ i.district+ ", " +i.state)
    print(locate)
    dataJSON = dumps(locate) # convert to JSON
    print(dataJSON)
    if request.user.is_authenticated:
        print('auth')
        return render(request, 'accounts/C_location.html', {'data':dataJSON})
    else:
        print('Not auth')
        return render(request, 'location.html', {'data':dataJSON})
def teams(request):
    if request.user.is_authenticated:
        print('Auth')
        return render(request, 'accounts/C_tems.html')
    else:
        print('Not auth')
        return render(request, 'tems.html')

@unauthenticated_user   
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print("YES")
        if user is not None:
            login(request, user)
            return redirect('CustomerProfile')
        else:
            messages.success(request, 'Username doesn\'t exist')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

def managerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print("YES")
        if user is not None:
            login(request, user)
            return redirect('ManagerProfile')
        else:
            messages.success(request, 'Username doesn\'t exist')
    return render(request, 'ManagerLogin.html')


@unauthenticated_user
def register(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
                name = username,
                email = email
            )
            messages.success(request, 'Account was created for ' + username)
            print("is saved")
            return redirect('loginUser')
        else:
            print('Not saved')
            messages.error(request,"Invalid fields")
    return render(request, 'register.html', {'form':form})
    

def book(request):
    list = {}
    pid_fetch = []
    forms = BookedForm()
    if request.method == "POST":
        forms = BookedForm(request.POST)
        if 'date' in request.POST:
            print("firstform")
            time = request.POST.get('date')
            timing = Scheduler.objects.filter(Date=time).values()
            id_val = Scheduler.objects.filter(Date=time).values('id')
            print(str(id_val))
            for i in id_val:
                pid_fetch.append(i.get('id'))
            print(type(pid_fetch))
            print(pid_fetch)
            pid_fetch = int(pid_fetch[0])

            for value in timing:
                if value.get('AM5') == True:
                    list.update({'seat1': 'hidden'})
                else:
                    list.update({'seat1': 'visible'})
            for value in timing:
                if value.get('AM5') == True:
                    list.update({'seat1': 'hidden'})
                else:
                    list.update({'seat1': 'visible'})
            for value in timing:
                if value.get('AM6') == True:
                    list.update({'seat2': 'hidden'})
                else:
                    list.update({'seat2': 'visible'})
            for value in timing:
                if value.get('AM7') == True:
                    list.update({'seat3': 'hidden'})
                else:
                    list.update({'seat3': 'visible'})
            for value in timing:
                if value.get('AM8') == True:
                    list.update({'seat4': 'hidden'})
                else:
                    list.update({'seat4': 'visible'})
            for value in timing:
                if value.get('AM9') == True:
                    list.update({'seat5': 'hidden'})
                else:
                    list.update({'seat5': 'visible'})
            for value in timing:
                if value.get('AM10') == True:
                    list.update({'seat6': 'hidden'})
                else:
                    list.update({'seat6': 'visible'})
            for value in timing:
                if value.get('AM11') == True:
                    list.update({'seat7': 'hidden'})
                else:
                    list.update({'seat7': 'visible'})
            for value in timing:
                if value.get('AM12') == True:
                    list.update({'seat8': 'hidden'})
                else:
                    list.update({'seat8': 'visible'})
            for value in timing:
                if value.get('PM1') == True:
                    list.update({'seat9': 'hidden'})
                else:
                    list.update({'seat9': 'visible'})
            for value in timing:
                if value.get('PM2') == True:
                    list.update({'seat10': 'hidden'})
                else:
                    list.update({'seat10': 'visible'})
            for value in timing:
                if value.get('PM3') == True:
                    list.update({'seat11': 'hidden'})
                else:
                    list.update({'seat11': 'visible'})
            for value in timing:
                if value.get('PM4') == True:
                    list.update({'seat12': 'hidden'})
                else:
                    list.update({'seat12': 'visible'})
            for value in timing:
                if value.get('PM5') == True:
                    list.update({'seat13': 'hidden'})
                else:
                    list.update({'seat13': 'visible'})
            for value in timing:
                if value.get('PM6') == True:
                    list.update({'seat14': 'hidden'})
                else:
                    list.update({'seat14': 'visible'})
            for value in timing:
                if value.get('PM7') == True:
                    list.update({'seat15': 'hidden'})
                else:
                    list.update({'seat15': 'visible'})
            for value in timing:
                if value.get('PM8') == True:
                    list.update({'seat16': 'hidden'})
                else:
                    list.update({'seat16': 'visible'})
            for value in timing:
                if value.get('PM9') == True:
                    list.update({'seat17': 'hidden'})
                else:
                    list.update({'seat17': 'visible'})
            for value in timing:
                if value.get('PM10') == True:
                    list.update({'seat18': 'hidden'})
                else:
                    list.update({'seat18': 'visible'})
            for value in timing:
                list.update({'dates': value.get('Date')})
            for value in timing:
                list.update({'id': value.get('id')})
            list.update({'hidden':'hidden'})

        if  'test' in request.POST:
            count = 0
            slot_list = ""
            ids = request.POST.get('test')
            sched = Scheduler.objects.get(id=ids)
            print(sched)
            if 'AM5' in request.POST:
                count+=1
                sched.AM5 = True
                slot_list = "5:00 AM  "
                sched.save()
            if 'AM6' in request.POST:
                count+=1
                sched.AM6 = True
                slot_list = slot_list + "6:00 AM  "
                sched.save()
            if 'AM7' in request.POST:
                count+=1
                sched.AM7 = True
                slot_list =slot_list + "7:00 AM  "
                sched.save()
            if 'AM8' in request.POST:
                count+=1
                sched.AM8 = True
                slot_list =slot_list + "8:00 AM  "
                sched.save()
            if 'AM9' in request.POST:
                count+=1
                sched.AM9 = True
                slot_list =slot_list + "9:00 AM  "
                sched.save()
            if 'AM10' in request.POST:
                count+=1
                sched.AM10 = True
                slot_list =slot_list + "10:00 AM  "
                sched.save()
            if 'AM11' in request.POST:
                count+=1
                sched.AM11 = True
                slot_list =slot_list + "11:00 AM  "
                sched.save()
            if 'AM12' in request.POST:
                count+=1
                sched.AM12 = True
                slot_list =slot_list + "12:00 AM  "
                sched.save()
            if 'PM1' in request.POST:
                count+=1
                sched.PM1 = True
                slot_list =slot_list + "1:00 PM  "
                sched.save()
            if 'PM2' in request.POST:
                count+=1
                sched.PM2 = True
                slot_list =slot_list + "2:00 PM  "
                sched.save()
            if 'PM3' in request.POST:
                count+=1
                sched.PM3 = True
                slot_list =slot_list + "3:00 PM  "
                sched.save()
            if 'PM4' in request.POST:
                count+=1
                sched.PM4 = True
                slot_list =slot_list + "4:00 PM  "
                sched.save()
            if 'PM5' in request.POST:
                count+=1
                sched.PM5 = True
                slot_list =slot_list + "5:00 PM  "
                sched.save()
            if 'PM6' in request.POST:
                count+=1
                sched.PM6 = True
                slot_list =slot_list + "6:00 PM  "
                sched.save()
            if 'PM7' in request.POST:
                count+=1
                sched.PM7 = True
                slot_list =slot_list + "7:00 PM  "
                sched.save()
            if 'PM8' in request.POST:
                count+=1
                sched.PM8 = True
                slot_list =slot_list + "8:00 PM  "
                sched.save()
            if 'PM9' in request.POST:
                count+=1
                sched.PM9 = True
                slot_list =slot_list + "9:00 PM  "
                sched.save()
            if 'PM10' in request.POST:
                count+=1
                sched.PM10 = True
                slot_list =slot_list + "10:00 PM  "
                sched.save()
        

            if forms.is_valid():
                forms.save()

            if forms.is_valid():
                name = request.POST['name']
                slot_fetch = Booked.objects.filter(name=name).values('id')
                slot = Booked.objects.get(id=slot_fetch[0]['id'])
                slot.slot_date = sched.Date
                slot.slot_time = slot_list
                slot.save()
                print(name)
            request.session['bill'] = count*500
            request.session['slots'] = slot_list
            print("succesfully updated : ", request.session['bill'])
            print('slot list : ', slot_list)
            return redirect('bills')
        
        if request.user.is_authenticated:
            print('auth')  
            return render(request, 'accounts/C_Form.html',{'list':list,'forms':forms})
        else:
            print('not auth')
            return render(request, 'Form.html',{'list':list,'forms':forms})
    if request.user.is_authenticated:
        print('auth')
        return render(request, 'accounts/C_Form.html',{'forms':forms})
    else:
        print('not auth')
        return render(request, 'Form.html',{'forms':forms})

def bills(request):
    print(request.session['bill'])
    print(request.session['slots'])
    if request.user.is_authenticated: 
        print('auth')
        return render(request, 'accounts/C_bills.html',{"bill": request.session['bill']})
    else:
        print('not auth')
        return render(request, 'bills.html',{"bill": request.session['bill']})



@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def CustomerProfile(request):
    return render(request, 'accounts/CustomerProfile.html')
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def CustomerBookingHistory(request):
    return render(request, 'accounts/CustomerBookingHistory.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def CustomerTransactionHistory(request):
    return render(request, 'accounts/CustomerTransactionHistory.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def Privacy(request):
    return render(request, 'accounts/Privacy.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def CustomerProfileSettings(request):
    username = request.user.customer.name
    email = request.user.customer.email
    address = request.user.customer.address
    phone = request.user.customer.phone
    print(username) 
    print(email)
    print(address)
    print(phone)
    contents = {'username':username, 'email':email,'address':address,'phone':phone}
    return render(request, 'accounts/CustomerProfileSettings.html', {'contents':contents})

##LOGIN MODE VIEWS


def C_index(request):
    return render(request, 'accounts/C_index.html')

def C_indoor(request):
    return render(request, 'accounts/C_indoor.html')

def C_outdoor(request):
    return render(request, 'accounts/C_outdoor.html')

def C_location(request):
    locs = Location.objects.all()
    locate = []
    for i in locs:
        locate.append(i.place+ ", " +i.local+ ", "+ i.district+ ", " +i.state)
    print(locate)
    dataJSON = dumps(locate) # convert to JSON
    print(dataJSON)
    return render(request, 'accounts/C_location.html', {'data':dataJSON})

def C_teams(request):
    return render(request, 'accounts/C_tems.html')

def ManagerProfile(request):
    return render(request, 'ManagerProfile.html')