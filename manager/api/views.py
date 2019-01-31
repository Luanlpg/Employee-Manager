from django.shortcuts import render
from django.http import Http404

from .serializer import EmployeeSerializer
from .serializer import EmployeeDetailSerializer

from .models import Employee

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

class EmployeeListView(APIView):
    """
    View que lista e cadastra Funcionário.
    """
    serializer_class = EmployeeSerializer
    serializer_detail_class = EmployeeDetailSerializer

    def get(self, request, format=None):
        serializer = self.serializer_detail_class(Employee.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    """
    View que mostra, altera e apaga Funcionário.
    """
    serializer_class = EmployeeSerializer

    def get_employee(self, name):
        try:
            name = name.replace('-', ' ')
            return Employee.objects.get(name=name)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        employee = self.get_employee(name)
        serializer = self.serializer_class(employee)
        return Response(serializer.data)

    def patch(self, request, name, format=None):
        employee = self.get_employee(name)
        serializer = self.serializer_class(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        employee = self.get_employee(name)
        employee.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
