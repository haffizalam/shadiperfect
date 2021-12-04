from django.urls import path,include
from .import views

app_name='admin01'
urlpatterns = [
    path('home/',views.home),
    #path('edit/',views.edit),
    path('religion/',views.add_religion),
    path('del_rel/<int:id>/',views.del_rel,name='del_rel'),
    path('city/',views.add_city),
    path('lang/',views.add_lang),
    path('admin_sign/',views.admin_sign),
    path('view_fbk/',views.view_fbk),
    path('add_story/',views.add_story),
    path('del_story/<int:id>/',views.del_story,name='del_story')

    


]
