

from . import views
from django.urls import path


# urlpatterns = [
#
#     path('',views.demo,name='demo'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact')
#     ]
# urlpatterns = [
#     path('',views.input1,name='input1'),
#     path('add/',views.addition,name='addition')
#     ]
urlpatterns = [
    path('',views.demo,name='demo')
    ]