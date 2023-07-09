from django.urls import path
from . import views

urlpatterns = [ 
path('', views.PizzeriaListAPIView.as_view(),name="pizzeria_list"), 
path('<int:id>/', views.PizzeriaRetrieveAPIView.as_view(),name="pizzeria_detail"),
path('create/', views.PizzerialCreateAPIView.as_view(),name="pizzeria_create"),
path('update/<int:id>/', views.PizzerialRetrieveUpdateAPIView.as_view(), name="pizzeria_update"),
path('delete/<int:id>/', views.PizzerialDestroyAPIView.as_view(),name="pizzeria_delete")

]