from .views import DealerCreateAPIView, DealerDetailAPIView, DealerListAPIView,\
    DealerUpdateAPIView, DealerDeleteAPIView
from django.urls import path, include

app_name = "Dealer"

urlpatterns = [
    path('', DealerListAPIView.as_view(), name='list'),
    path('detail/<pk>', DealerDetailAPIView.as_view()),
    path('delete/<pk>', DealerDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', DealerUpdateAPIView.as_view(), name='update'),
    path('create/', DealerCreateAPIView.as_view(), name='create')
]