from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("tb/<int:id>",views.textbook,name="textbook"),
    path("syllab/<int:id>", views.syllab, name="syllab")
]