from django.conf.urls import url

from . import views

urlpatterns=[
url(r'^$', views.index ,name='index'),
url(r'^enter_expenditure/', views.enter_expenditure, name='enter_expenditure'),
url(r'^enter_sundryexpense', views.enter_sundryexpense ,name='enter_sundryexpense'),
url(r'^pay_salary/', views.pay_salary, name='pay_salary'),

url(r'^sundryreport', views.sundryreport ,name='sundryreport'),
url(r'^salaryreport/', views.salaryreport, name='salaryreport'),
url(r'^expenditurereport/', views.expenditurereport, name='expenditurereport'),


url(r'^salariespdf/', views.salariespdf.as_view() ,name='salariespdf'),
url(r'^sundrypdf/', views.sundrypdf.as_view() ,name='sundrypdf'),
url(r'^expenditurepdf/', views.expenditurepdf.as_view() ,name='expenditurepdf'),

url(r'^expensereceipt/(?P<pk>\d+)', views.expensereceipt.as_view() ,name='expensereceipt'),
url(r'^salaryreceipt/(?P<pk>\d+)', views.salaryreceipt.as_view() ,name='salaryreceipt'),
url(r'^sundryreceipt/(?P<pk>\d+)', views.sundryreceipt.as_view() ,name='sundryreceipt'),

url(r'^expenditurearchive/', views.expenditurearchive, name='expenditurearchive'),
url(r'^salaryarchive/', views.salaryarchive, name='salaryarchive'),
url(r'^sundryarchive/', views.sundryarchive, name='sundryarchive'),

url(r'^expenditurearchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.expenditurearchivepdf.as_view(), name='expenditurearchivepdf'),
url(r'^salaryarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.salaryarchivepdf.as_view(), name='salaryarchivepdf'),
url(r'^sundryarchivepdf/(?P<report_month>.+?)/(?P<report_year>.+?)/', views.sundryarchivepdf.as_view(), name='sundryarchivepdf'),

url(r'^edit_payment/(?P<pk>\d+)', views.edit_payment ,name='edit_payment'),
url(r'^delete_payment/(?P<pk>\d+)', views.delete_payment ,name='delete_payment'),
url(r'^edit_salary/(?P<pk>\d+)', views.edit_salary ,name='edit_salary'),
url(r'^delete_salary/(?P<pk>\d+)', views.delete_salary ,name='delete_salary'),
url(r'^edit_sundry/(?P<pk>\d+)', views.edit_sundry ,name='edit_sundry'),
url(r'^delete_sundry/(?P<pk>\d+)', views.delete_sundry ,name='delete_sundry'),

url(r'^salaryreport/', views.salaryreport, name='salaryreport'),
url(r'^expenditurereport/', views.expenditurereport, name='expenditurereport'),

url(r'^expensesarchivessearch/', views.expensesarchivessearch, name='expensesarchivessearch'),
url(r'^salaryarchivessearch/', views.salaryarchivessearch, name='salaryarchivessearch'),
url(r'^sundrysarchivessearch/', views.sundryarchivessearch, name='sundryarchivessearch'),
#url(r'^expenditure_report_archive/', views.expenditure_report_archive, name='expenditure_report_archive'),
]