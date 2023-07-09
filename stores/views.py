from django.shortcuts import render
from rest_framework import generics
from .serializer import PizzeriaListSerializer,PizzerialDetailSerializer
from .models import Pizzeria


class PizzeriaListAPIView(generics.ListAPIView):
    queryset=Pizzeria.objects.all()
    serializer_class =PizzeriaListSerializer
    
class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field="id"
    queryset=Pizzeria.objects.all()
    serializer_class =PizzerialDetailSerializer
    
class PizzerialCreateAPIView(generics.CreateAPIView):
    queryset=Pizzeria.objects.all()
    serializer_class=PizzerialDetailSerializer
    
class PizzerialRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field="id"
    queryset=Pizzeria.objects.all()
    serializer_class=PizzerialDetailSerializer
class PizzerialDestroyAPIView(generics.DestroyAPIView):
    lookup_field="id"
    queryset=Pizzeria.objects.all()
    