from django.urls import path

from new_app1 import views

urlpatterns = [
    path("",views.test1,name="test1"),
    path("index",views.test2,name="test1")

]