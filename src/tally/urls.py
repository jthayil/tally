"""pvlin URL Configuration
    path('', views.home, name='home')
    path('', Home.as_view(), name='home')
    path('blog/', include('blog.urls'))
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
