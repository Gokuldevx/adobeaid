"""home_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home_app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('home/',home,name="home"),
    path('about/',about,name="about"),
    path('cregister/',cregister,name="cregister"),
    path('addstaff/',addstaff,name="addstaff"),
    path('spregister/',spregister,name="spregister"),
    path('ulogin/',ulogin,name="ulogin"),
    path('adminhome/',admin_home,name="adminhome"),
    path('cregisteraction/',cregisteraction,name="cregisteraction"),
    path('addstaffaction/',addstaffaction,name="addstaffaction"),
    path('spregisteraction/',spregisteraction,name="spregisteraction"),
    path('loginaction/',loginaction,name="loginaction"),
    path('viewcust/',view_cust,name="viewcust"),
    path('viewstaff/',view_staff,name="viewstaff"),
    path('viewsp/',view_sp,name="viewsp"),
    path('editcustprofile/',edit_custprofile,name="editcustprofile"),
    path('custhome/',cust_home,name="custhome"),
    path('editstaffprofile/',edit_staffprofile,name="editstaffprofile"),
    path('staffhome/',staff_home,name="staffhome"),
    path('editspprofile/',edit_spprofile,name="editspprofile"),
    path('sphome/',sp_home,name="sphome"),
    path('approvestaff/',approve_staff,name="approvestaff"),
    path('rejectstaff/',reject_staff,name="rejectstaff"),
    path('approvesp/',approve_sp,name="approvesp"),
    path('rejectsp/',reject_sp,name="rejectsp"),
    path('editcustprofileaction/',edit_cust_profileaction,name="editcustprofileaction"),
    path('editspprofileaction/',edit_sp_profileaction,name="editspprofileaction"),
    path('editstaffprofileaction/',edit_staff_profileaction,name="editstaffprofileaction"),
    path('services/',services,name="services"),
    path('servicesaction/',servicesaction,name="servicesaction"),
    path('deleteservices/',delete_services,name="deleteservices"),
    path('deletecustacc/',delete_custacc,name="deletecustacc"),
    path('deletespacc/',delete_spacc,name="deletespacc"),
    path('removestaff/',remove_staff,name="removestaff"),
    path('viewservices/',view_services,name="viewservices"),
    path('subservices/',subservices,name="subservices"),
    path('subserviceaction/',subserviceaction,name="subserviceaction"),
    path('servicelist/',servicelist,name="servicelist"),
    path('searchaction/',searchaction,name="searchaction"),
    path('viewsub/',viewsub,name="viewsub"),
    path('book/',book,name="book"),
    path('bookaction/',bookaction,name="bookaction"),
    path('pendingservice/',pendingservice,name="pendingservicebook"),
    path('tapr/',tapr,name="tapr"),
    path('porder/',porder,name="porder"),
    path('assign/',assign,name="assign"),
    path('cvbook/',cvbook,name="cvbook"),
    path('pay/',pay,name="pay"),
    path('cpaid/',cpaid,name="cpaid"),
    path('aorder/',aorder,name="aorder"),
    path('status/',status,name="status"),
    path('astatus/',astatus,name="astatus"),
    path('sstatus/',sstatus,name="sstatus"),
    path('myservice/',myservice,name="myservice"),
    path('feedback/',feedback,name="feedback"),
    path('faction/',faction,name="faction"),
    path('vfeedback/',vfeedback,name="vfeedback"),
    path('updser/',updser,name="updser"),
    path('updseract/',updseract,name="updseract"),
    path('orderreport/',orderreport,name="orderreport"),
    path('vbstatus/',vbstatus,name="vbstatus"),
    path('avbstatus/',avbstatus,name="avbstatus"),
    path('uReview/',uReview,name="uReview"),
    path('uReviewAct/',uReviewAct,name="uReviewAct"),
    path('uvReview/',uvReview,name="uvReview"),
    path('rstatus/',rstatus,name="rstatus"),
    path('cancel/',cancel,name="cancel"),
    path('sorderreport/',sorderreport,name="sorderreport"),
    path('remark/',remark,name="remark"),
    path('bank/',bank,name="bank"),
    path('bankaction/',bankaction,name="bankaction"),
    path('preBookingAct/',preBookingAct,name="preBookingAct"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=staticfiles_urlpatterns()

