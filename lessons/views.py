from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from lessons.models import Booking, RequestForLessons
from .forms import RequestForLessonsForm, StudentSignUpForm, PaymentForm
from django.contrib.auth import authenticate, login, logout
from .forms import LogInForm
from .models import Booking , Invoice
from django.http import HttpResponseForbidden

# # Create your views here.
def home(request):
    return render(request, "home.html")

def sign_up(request):
    # form = SignUpForm()
    return render(request, "sign_up.html")

def sign_up_student(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            # create user and add to db
            form.save()
            return redirect("home")
            # login(request, user)
            # return redirect("feed")
    else:
        form = StudentSignUpForm()
    return render(request, "sign_up_student.html", {"form": form})


def log_in(request):
    form = LogInForm()
    return render(request, "log_in.html", {"form": form})

@login_required
def booking_list(request):
    bookings = Booking.objects.all() # Gets all existing booking not specific to user logged in
    return render(request, 'booking_list.html', {'bookings': bookings})

# @login_required
# def booking_list(request):
#     if request.user.is_student is False:
#         return redirect("home")
    
#     bookings = request.user.student.booking_set.all()
    
#     return render(request, 'booking_list.html', {'bookings': bookings})
    
@login_required
def show_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except ObjectDoesNotExist:
        return redirect('bookings')
    else:
        return render(request, 'show_booking.html', {'booking' : booking})

def log_out(request):
    logout(request)
    return redirect(home)
  
@login_required
def requests_list(request):
    requests = RequestForLessons.objects.filter(student=request.user)
    return render(request, "requests_list.html", {"requests": requests})


@login_required
def create_request(request):
    if request.method == "POST":
        form = RequestForLessonsForm(request.POST, usr=request.user)
        if form.is_valid():
            req = form.save()
            print(req)
            return redirect("home")

    form = RequestForLessonsForm(usr=request.user)
    return render(request, "create_request.html", {"form": form})

@login_required
def payment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            form = PaymentForm(request.POST)
            if form.is_valid():
                invoice = Invoice.objects.get(urn=form.cleaned_data.get("invoice_urn"))
                invoice.is_paid = True
                return redirect('home')
            else:
                return render(request, 'home.html', {'form': form}) # replace with actual feed page
        else:
            return redirect('log_in')
    else:
        return HttpResponseForbidden()
