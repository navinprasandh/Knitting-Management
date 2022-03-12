
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('reg/',views.reg.as_view(),name="reg"),
    path('wstat/',views.wstatus,name="wstat"),
]
