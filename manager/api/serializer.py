from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializados de funcionário.
    """
    class Meta:
        model = Employee
        depth = 1
        fields = [
            'name',
            'email',
            'department'
            ]

class EmployeeDetailSerializer(serializers.ModelSerializer):
    """
    Serializador de funcionário que traz departamento.
    """
    class Meta:
        model = Employee
        depth = 1
        fields = [
            'name',
            'email',
            'department',
            'link'
            ]
