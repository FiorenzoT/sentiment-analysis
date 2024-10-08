from django.urls import path
from application import views

urlpatterns = [
    path('', views.sentiment_analysis, name='sentiment_analysis'),
    path('history/', views.sentiment_history, name='sentiment_history'),
]