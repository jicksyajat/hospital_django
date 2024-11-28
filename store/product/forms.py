from django import forms
from .models import Booking


class Dateinput(forms.DateInput):
    input_type= 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets ={
            'booking_date': Dateinput(),
        }

        labels={
            'p_name' : "Patients Name",
            'p_phone' :"Patients Phone",
            'p_email' :"Patients Email",
            'booking_date' : "Booking Date",
        }



# login creation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name')
