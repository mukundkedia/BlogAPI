from django.urls import path
from .views import BlogAPIView,BlogDetail

urlpatterns = [
    # path('',views.BlogContent.as_view()),
    # path('<int:pk>/',views.BlogData.as_view())
    path('',BlogAPIView.as_view()),
    path('<int:id>/',BlogDetail.as_view())
]