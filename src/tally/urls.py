"""pvlin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from tally import views

urlpatterns = [
    path("", views.home, name="home"),
    path("drs_report/list/", views.drsreportlist, name="drsreportlist"),
    path("drs_report/detail/<int:pk>/",
         views.drsreportdetail, name="drsreportdetail"),
    path("drs_report/create/", views.drsreportcreate, name="drsreportcreate"),
    path("drs_report/update/<int:pk>/",
         views.drsreportupdate, name="drsreportupdate"),
    path("drs_report/delete/<int:pk>/",
         views.drsreportselete, name="drsreportselete"),
]
