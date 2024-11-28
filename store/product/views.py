from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def home(request):
    return render(request,'home.html')

from django.urls import reverse
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        
            
    return render(request,'pages/register.html',{'form':form})



def department(request):
    dict1={'dept': DEPARTMENT.objects.all()}
    return render(request,'department.html',dict1)


def doctor(request):
    dict_docs ={
        'doctors' : Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)




from .forms import BookingForm

def bookingss(request):
    form=BookingForm()
    if request.method =="POST":
        print("Sucessful")
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print("Sucessful")
            return redirect(reverse('home'))
    
    return render(request,'booking.html',{'form':form})





