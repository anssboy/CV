
from django.urls import path
from page.views import *

app_name = 'webapp'

urlpatterns = [
    #     url adress  views
    path('', index, name='home'),
]
