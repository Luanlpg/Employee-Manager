from django.urls import path
from django.urls import include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('employee/', views.EmployeeListView.as_view(), name='employee'),
    path('employee/<str:name>/', views.EmployeeDetailView.as_view()),
]
