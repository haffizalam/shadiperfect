from django.urls import path,include
from .import views

app_name='app01'
urlpatterns = [
    path('home/',views.home),
    path('myprofile/',views.myprofile),
    path('add_data/',views.add_data),
    path('show/<int:id>/',views.show,name='show'),
    path('update_details/',views.update_details,name='update_details'),
    path('update_pro/<int:id>/',views.update_pro,name='update_pro'),
    path('cat_search/<str:name>/',views.cat_search,name='cat_search'),
    path('chnge_passwd/',views.chnge_passwd,name='chnge_passwd'),
    path('deactivate/',views.deactivate),
    path('search1/',views.search1,name='search1'),
    

    #path('update_pro/<int:id>/',views.update_pro,name='update_pro')

]
