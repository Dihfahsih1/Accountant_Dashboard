from django import forms
from .models import *


class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount','AmountInWords', 'ReceivedBy', 'ApprovedBy')

class SundryForm(forms.ModelForm):
    class Meta:
        model=Sundry
        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount','AmountInWords')

class SalaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        fields = ('Date','Staff','Salary_Type','Month','Amount','AmountInWords')

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('image','FistName','SecondName','Salary','Role','Duties','Sex','Contact')

