#uygula icerisinde bir url yapisi oluusturup onu da ana uygula icerisine tanitmak icin bu urls dosyasini olusturduk
#http://127.0.0.1:8000/

from django.urls import path
from. import views
#to reach method of the views

#http://127.0.0.1:8000/  - index
#http://127.0.0.1:8000/field/5  - The specified record in the database will be returned


#The expression to be added to the end of the path is written in quotes.
#this two url return homepage 
urlpatterns = [
    path('send_info/', views.send_info, name='send_info'),
    
    path('send_message/', views.send_message, name='send_message'),
    
    path("", views.index),
    path("index", views.index, name='index'),

  
    path("services/", views.services, name='services'),  
    path('subscription/', views.subscription, name='subscription'),
    path("appointment/", views.appointment, name='appointment'),  
    
   
    
    path('photos/', views.photos, name='photos'),
    path("wedding/", views.wedding, name='wedding'),  


   
    ]
    
 
