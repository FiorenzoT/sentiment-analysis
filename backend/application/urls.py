from django.urls import path
from application import views

urlpatterns = [
    path('', views.sentiment_analysis, name='sentiment_analysis')
]