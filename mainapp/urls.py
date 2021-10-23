from django.urls import path
from .views import MainIndex, hiha_form_post

app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('hiha/', hiha_form_post, name='post')
]