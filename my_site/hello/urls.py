from django.urls import path

from . import views
urlpatterns = [
    path("", views.index,name="index"),
    path("yuval", views.yuval,name="yuval"),
    path("<str:name>", views.greet,name="greet"),
    

]
