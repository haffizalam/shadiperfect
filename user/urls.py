from django.urls import path,include
from .import views

app_name='user'
urlpatterns = [
    path('home/',views.home),
    path('myprofile/',views.myprofile)
    #path('update_pro/<int:id>/',views.update_pro,name='update_pro')

]
