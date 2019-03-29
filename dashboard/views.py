#views
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View

from .forms import *
from .models import *
from .render import Render



def index(request):
    return render(request,'Accprofile.html')

    ####################################################
    #        ENTERING RECORDS INTO THE DATABASE        #
    ####################################################
# Adding Staff
 # payment of salaries
def pay_salary(request):
    if request.method=="POST":
        form=SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salaryreceipt')
    else:
        form=SalaryForm()
        return render(request, 'add_new.html',{'form':form})



def enter_expenditure(request):
    if request.method=="POST":
        form=SpendForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect ('enter_expenditure')
    else:
        form=SpendForm()
        items = Spend.objects.all()
        context = {'items': items, 'form': form, }
        return render(request, 'pay_expenditure.html',context)

def enter_sundryexpense(request):
    if request.method == "POST":
        form = SundryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sundryreceipt')
    else:
        form = SundryForm()
        return render(request, 'add_new.html', {'form': form})
#####################################################################
# EDITING, DELETING AND PRINTING OF RECEIPT OF EACH TRANSACTION MADE #
#####################################################################

def edit_payment(request, pk):
    item = get_object_or_404(Spend, pk=pk)
    if request.method == "POST":
        form = SpendForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('enter_expenditure')
    else:
        form = SpendForm(instance=item)
    return render(request, 'pay_expenditure.html', {'form': form, })
def delete_payment(request,pk):
    items= Spend.objects.filter(id=pk).delete()
    context = { 'items':items}
    return render(request, 'expenditureindex.html', context)

def edit_salary(request, pk):
    item = get_object_or_404(Salary, pk=pk)
    if request.method == "POST":
        form = SalaryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('pay_salary')
    else:
        form = SpendForm(instance=item)
    return render(request, 'add_new.html', {'form': form, })
def delete_salary(request,pk):
    items= Spend.objects.filter(id=pk).delete()
    context = { 'items':items}
    return render(request, 'salaryindex.html', context)

def edit_sundry(request, pk):
    item = get_object_or_404(Sundry, pk=pk)
    if request.method == "POST":
        form = SundryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('enter_sundryexpense')
    else:
        form = SundryForm(instance=item)
    return render(request, 'add_new.html', {'form': form, })

def delete_sundry(request, pk):
    items = Sundry.objects.filter(id=pk).delete()
    context = {'items': items}
    return render(request, 'sundryindex.html', context)

       ####################################################
      #        GENERATING REPORTS IN FORM OF PDFS         #
      ####################################################

#Printing Expenditure Report
class expenditurepdf(View):
    def get(self, request):
        current_month = datetime.now().month
        expense = Spend.objects.filter(Date__month=current_month).order_by('-Date')

        today = timezone.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in expense:
            totalexpense += instance.Amount
        expensecontext ={

            'month': month,
            'today':today,
            'expense':expense,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('expenditurepdf.html',expensecontext)

#Printing Salaries Report
class salariespdf(View):
    def get(self, request):
        current_month = datetime.now().month
        salaries = Salary.objects.filter(Date__month=current_month).order_by('-Date')
        today = timezone.now()
        month = today.strftime('%B')
        totalsalary = 0
        for instance in salaries:
            totalsalary += instance.Amount
        salarycontext ={
            'month': month,
            'today':today,
            'salaries':salaries,
            'request': request,
            'totalsalary': totalsalary,
        }
        return Render.render('pdf.html',salarycontext)

#Printing Sundry Expenses Report
class sundrypdf(View):
    def get(self, request):
        current_month = datetime.now().month
        sundry = Sundry.objects.all()
        today = timezone.now()
        month = today.strftime('%B')
        totalsundry = 0
        for instance in sundry:
            totalsundry += instance.Amount
        sundrycontext ={
            ''
            'month': month,
            'today':today,
            'sundry':sundry,
            'request': request,
            'totalsundry': totalsundry,
        }
        return Render.render('sundrypdf.html',sundrycontext)

        ####################################################
        #        ARCHIVING OF THE MONTHLY REPORTS          #
        ####################################################


def salaryarchive(request):
    salaryarchived = SalaryReportArchive.objects.all().order_by('-Date')
    total = SalaryReportArchive.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
        'total_amount':total_amount,
        'salaryarchived': salaryarchived
               }
    return render(request, 'salaryarchive.html', context)

def expenditurearchive(request):
    expensesarchived = ExpensesReportArchive.objects.all().order_by('-Date')
    total = SalaryReportArchive.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
        'total_amount':total_amount,
        'expensesarchived':expensesarchived
    }
    return render(request, 'expenditurearchive.html', context)


        # calculating totals in sundryexpense report
def sundryarchive(request):
    sundryarchived = SundryReportArchive.objects.all().order_by('-Date')
    total = SundryReportArchive.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
        'total_amount':total_amount,
        'sundryarchived': sundryarchived
               }
    return render(request, 'sundryarchive.html', context)





 ####################################################
#       PRINTING THE RECEIPTS                        #
 ####################################################

class expensereceipt(View):
    def get(self, request, pk):
        expense = get_object_or_404(Spend,pk=pk)
        today = timezone.now()
        expensecontext = {
            'today': today,
            'expense': expense,
            'request': request,
        }
        return Render.render('expensereceipt.html', expensecontext)

class salaryreceipt(View):
    def get(self, request, pk):
        salary= get_object_or_404(Salary,pk=pk)
        today = timezone.now()
        salarycontext = {
            'today': today,
            'salary': salary,
            'request': request,
        }
        return Render.render('salaryreceipt.html', salarycontext)

class sundryreceipt(View):
    def get(self, request, pk):
        sundry = get_object_or_404(Sundry,pk=pk)
        today = timezone.now()
        sundrycontext = {
            'today': today,
            'sundry': sundry,
            'request': request,
        }
        return Render.render('sundryreceipt.html', sundrycontext)


    ############################################################
   # SUBMISSION OF MONTHLY REPORTS TO BE ARCHIVED              #
    ############################################################

#####################
# EXPENSES ARCHIVING#
#####################
def expenditurereport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']

        #all the available expense in the expenses table
        all_expenses = Spend.objects.all()

        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            reason=expense.ReasonForPayment
            name=expense.PaymentMadeTo

            # the expense archive object
            expense_archiveobj=ExpensesReportArchive()

            #attached values to expense_archiveobj
            expense_archiveobj.Name=name
            expense_archiveobj.Date=date
            expense_archiveobj.Amount=amount
            expense_archiveobj.Reason=reason
            expense_archiveobj.year=archived_year
            expense_archiveobj.month=archived_month

            expense_archiveobj.save()

        #deleting all the expense from reports table


        #paid = Spend.objects.all().aggregate(Sum('Amount'))
        all_expenses.delete()

        message="The expenses report has been made"
        context={
                 'message':message,
                 }

        return render(request, 'expenditureindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'August', 'September',
              'October', 'November',
              'December']
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    items =Spend.objects.all()
    total = Spend.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
         'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,


    }
    return render(request, 'expenditureindex.html', context)

def salaryreport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']

        #all the available expense in the expenses table
        all_expenses = Salary.objects.all()
        for expense in all_expenses:
            date=expense.Date
            Manth = expense.Month
            amount=expense.Amount
            salary_type=expense.Salary_Type
            name = expense.Staff

            # the expense archive object
            expense_archiveobj=SalaryReportArchive()

            #attached values to expense_archiveobj
            expense_archiveobj.Staff = name
            expense_archiveobj.Date=date
            expense_archiveobj.Month=Manth
            expense_archiveobj.Amount=amount
            expense_archiveobj.Salary_Type=salary_type
            expense_archiveobj.archivedyear= archived_year
            expense_archiveobj.archivedmonth =archived_month

            expense_archiveobj.save()

        #deleting all the expense from reports table
        all_expenses.delete()

        message="The expenses report has been made"
        context={'message':message}

        return render(request, 'salaryindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'August', 'September',
              'October', 'November',
              'December']
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    total = Salary.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    items =Salary.objects.all()
    context = {
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,
    }
    return render(request, 'salaryindex.html', context)

def sundryreport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        #all the available expense in the expenses table
        all_expenses = Sundry.objects.all()
        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            reason=expense.ReasonForPayment
            name=expense.PaymentMadeTo

            # the expense archive object
            expense_archiveobj=SundryReportArchive()

            #attached values to expense_archiveobj
            expense_archiveobj.Name=name
            expense_archiveobj.Date=date
            expense_archiveobj.Amount=amount
            expense_archiveobj.Reason=reason
            expense_archiveobj.year=archived_year
            expense_archiveobj.month=archived_month

            expense_archiveobj.save()

        #deleting all the expense from reports table
        all_expenses.delete()

        message="The expenses report has been made"
        context={'message':message}

        return render(request, 'sundryindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'August', 'September',
              'October', 'November',
              'December']
    years = [2019, 2020, 2021]

    total = Sundry.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    items =Sundry.objects.all()
    context = {
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,
    }
    return render(request, 'sundryindex.html', context)

# searching for the archives
def expensesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October', 'November','December']
        years = [2018, 2019, 2020, 2021]
        today = timezone.now()
        archived_reports = ExpensesReportArchive.objects.filter(month=report_month, year=report_year)
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]


        context = {'archived_reports':archived_reports,
                   'months': months,
                   'years': years,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "expenditurearchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'August', 'September','October', 'November', 'November', 'December']
    years = [2018, 2019, 2020, 2021]
    expenses=ExpensesReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'expenses': expenses}
    return render(request, "expenditurearchive.html", context)


def salaryarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SalaryReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October',  'November','December']
        years = [2018, 2019, 2020, 2021]

        salary = SalaryReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]

        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'expenses':salary,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "salaryarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'August', 'September','October',  'November', 'December']
    years = [2018, 2019, 2020, 2021]

    salary=SalaryReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'salary': salary}
    return render(request, "salaryarchive.html", context)

def sundryarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SundryReportArchive.objects.filter(month=report_month, year=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October', 'November','December']
        years = [2019, 2020, 2021]

        sundry = SundryReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]

        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'expenses':sundry,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "sundryarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'August', 'September','October', 'November', 'November', 'December']
    years = [2019, 2020, 2021]

    sundry=SundryReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'sundry': sundry}
    return render(request, "sundryarchive.html", context)



    ###############################################
    # GENERATING REPORTS IN FORM OF ANNUAL PDFS   #
    ###############################################


# Printing Expenditure archived Report
class expenditurearchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_expenses = ExpensesReportArchive.objects.filter(month=report_month, year=report_year)
        today = timezone.now()
        month = today.strftime('%B')
        total = archived_expenses.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        expensecontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_expenses': archived_expenses,
            'report_year': report_year,
            'report_month': report_month
        }
        return Render.render('expenditurearchivepdf.html', expensecontext)


# Printing Salaries archived Report
class salaryarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_salary = SalaryReportArchive.objects.filter(month=report_month, year=report_year)
        today = timezone.now()
        total = archived_salary.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        salarycontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_salary': archived_salary,
        }
        return Render.render('salaryarchivepdf.html', salarycontext)


# Printing Sundry Expenses archived Report
class sundryarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_sundry = SundryReportArchive.objects.filter(month=report_month, year=report_year)
        today = timezone.now()
        month = today.strftime('%B')
        total = archived_sundry.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        sundrycontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_sundry': archived_sundry,
        }
        return Render.render('sundryarchivepdf.html', sundrycontext)