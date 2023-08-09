from django.urls import path
from . import views

#Urls paths
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register,name='register'),
    path('add',views.add,name='add')
]