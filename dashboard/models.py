from django.utils.timezone import now
from django.db import models
from django.db.models import Model
from django.db.models import Sum

class StaffDetails(models.Model):
    image = models.ImageField(upload_to="media", default="Photo")
    FistName= models.CharField(max_length=150, default="1st name",blank=False)
    SecondName = models.CharField(max_length=150, default="2nd name",blank=False)
    Salary = models.IntegerField(default=0)
    choices=(('Developers','ICT'),
        ('Receptionist', 'Rec'),
        ('Director', 'DIR'),
        ('Operations', 'CEO'),
        ('Cashiers', 'Cashier'),
        ('Executive', 'Exe'),)
    Role = models.CharField(max_length=20, default="MALE", blank=False, choices=choices)
    Duties = models.TextField(max_length=1000, default="ICT", blank=False)
    choices=(
        ('Male','Male'),
        ('Female', 'Female'))
    Sex = models.CharField(max_length=7, default="MALE", blank=False, choices=choices)
    Contact = models.CharField(max_length=100, default="Tel or Email")
    def __str__(self):
        return self.FistName + ' ' + self.SecondName


class Salary(models.Model):
    choices = (
        ('ALLOWANCE','Pay Allowances'),
        ('Salary','Monthly Salary'),
        ('Advance', 'Pay Advances'),
        ('Commission', 'Pay Commission')
    )
    months = (
        ('January','January'),('February','February'),('March', 'March'),('April', 'April')
        ,('May','May'),('June', 'June'),('July', 'July'),('August','August'),
        ('September', 'September'),('October', 'October'),('November','November'),('December', 'December')
    )
    Date = models.DateField(default=now())
    Salary_Type = models.CharField( max_length=12,choices=choices,default="SALARY")
    Staff = models.ForeignKey(StaffDetails,on_delete=models.CASCADE, blank=False)
    Month = models.CharField(max_length=12,choices=months, default="Month of Pay")
    Amount = models.IntegerField(default=0)
    AmountInWords = models.TextField(max_length=500, blank=False, default='amount in words')
    def __str__(self):
        return self.Staff

class Sundry(Model):
    Date = models.DateField(default=now())
    PaymentMadeTo = models.CharField(max_length=100, default="Canon", blank=False)
    ReasonForPayment = models.TextField(max_length=25, default="Only relatively small expense")
    Amount = models.IntegerField(default=0)
    AmountInWords = models.TextField(max_length=500, blank=False, default='amount in words')
    def __str__(self):
        return self.PaymentMadeTo

class Spend(models.Model):
    reason=(
        ('Mechanic','Car Repairing'),('WaterBills','Water Bills'),('Electricity','Electricity Bills'),('URA','Paying Revenue')
    )
    Date = models.DateField(default=now())
    PaymentMadeTo = models.CharField(max_length=100, default="Canon", blank=False)
    ReasonForPayment = models.CharField(max_length=100, choices=reason)
    Amount = models.IntegerField(default=0)
    AmountInWords = models.TextField(max_length=500, blank=False)
    ReceivedBy = models.CharField(max_length=100, blank=False)
    ApprovedBy = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'Name:{0}, Reason:{1}, Amount: {2}'.format(self.PaymentMadeTo, self.ReasonForPayment, self.Amount)

##########################################
#REPORT ARCHIVING MODELS AFTER SUBMISSION #
##########################################
class ExpensesReportArchive(models.Model):
    Date = models.DateField(default=now())
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(default=0.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    ReceivedBy = models.CharField(max_length=100, blank=False, default="Name")
    ApprovedBy = models.CharField(max_length=100, blank=False,default="Name")
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)
class SundryReportArchive(models.Model):
    Date = models.DateField(default=now())
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(default=0.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    ReceivedBy = models.CharField(max_length=100, blank=False, default="Name")
    ApprovedBy = models.CharField(max_length=100, blank=False, default="Name")
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)

class SalaryReportArchive(models.Model):
    Date = models.DateField(default=now())
    Salary_Type = models.CharField(max_length=100,null=True)
    Staff = models.CharField( max_length=100,null=True)
    Month = models.CharField(max_length=100,null=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Staff, self.Amount)