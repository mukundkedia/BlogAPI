from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogContent.as_view()),
    path('<int:pk>/',views.BlogData.as_view())
]