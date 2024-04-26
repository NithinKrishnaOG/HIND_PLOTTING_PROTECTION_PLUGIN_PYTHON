
from django.urls import path
from . import views



urlpatterns = [

path('', views.home, name='home'),
path('home', views.home, name='home'),
path('viewproductbl', views.viewproductbl, name='viewproductbl'),
path('signup', views.signup, name='signup'),
path('signupvalidator', views.signupvalidator, name='signupvalidator'),
path('login', views.login, name='login'),
path('loginvalidator', views.loginvalidator, name='loginvalidator'),
path('userhome', views.userhome, name='userhome'),
path('myaccount', views.myaccount, name='myaccount'),
path('edit_profile', views.edit_profile, name='edit_profile'),
path('editprofilevalidator', views.editprofilevalidator, name='editprofilevalidator'),
path('changepaswd', views.changepaswd, name='changepaswd'),
path('changepaswdvalidator', views.changepaswdvalidator, name='changepaswdvalidator'),
path('viewcart', views.viewcart, name='viewcart'),
path('search', views.search, name='search'),
path('viewproductal', views.viewproductal, name='viewproductal'),
path('addtocart', views.addtocart, name='addtocart'),
path('removecart', views.removecart, name='removecart'),
path('track', views.track, name='track'),
path('feedback', views.feedback, name='feedback'),
path('feedbackhandler', views.feedbackhandler, name='feedbackhandler'),
path('paymentlogin', views.paymentlogin, name='paymentlogin'),
path('paymentloginvalidator', views.paymentloginvalidator, name='paymentloginvalidator'),
path('paymentloginvalidator2', views.paymentloginvalidator2, name='paymentloginvalidator2'),
path('paymentupdate', views.paymentupdate, name='paymentupdate'),
path('searchbyname', views.searchbyname, name='searchbyname'),

###########
path('bankhome', views.bankhome, name='bankhome'),
path('banksignup', views.banksignup, name='banksignup'),
path('banksignupvalidator', views.banksignupvalidator, name='banksignupvalidator'),
path('banklogin', views.banklogin, name='banklogin'),
path('bankloginvalidator', views.bankloginvalidator, name='bankloginvalidator'),
path('editbankuser', views.editbankuser, name='editbankuser'),
############
path('adminhome', views.adminhome, name='adminhome'),
path('adminloginvalidator', views.adminloginvalidator, name='adminloginvalidator'),
path('viewcus', views.viewcus, name='viewcus'),
path('viewpayment', views.viewpayment, name='viewpayment'),
path('viewfeedback', views.viewfeedback, name='viewfeedback'),
path('insert', views.insert, name='insert'),
path('inserthandler', views.inserthandler, name='inserthandler'),
path('update', views.update, name='update'),
path('update1', views.update1, name='update1'),
path('update2', views.update2, name='update2'),
path('update2handler', views.update2handler, name='update2handler'),
path('delete', views.delete, name='delete'),
path('delete1', views.delete1, name='delete1'),
path('delp', views.delp, name='delp'),












]


