from django.urls import path
from . import views   # импортируем представления из текущего приложения

urlpatterns = [
    path('', views.resume_view, name='resume'),   # пустой путь – это главная страница
]