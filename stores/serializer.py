from rest_framework import serializers
from .models import Pizzeria
 
class PizzeriaListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pizzeria
            fields = [
            'id',
            'logo_image',
            'pizzeria_name',
            'city',
            'zip_code',
            
            ]
            
class PizzerialDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pizzeria
            fields = [
            'id',
            'logo_image',
            'pizzeria_name',
            'street',
            'state',
            'city',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active'
            
            ]