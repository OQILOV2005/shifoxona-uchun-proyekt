from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DepartamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"



class BemorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bemor
        fields = "__all__"


class Bemor_tolovSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bemor_tolov
        fields = "__all__"


class CassaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"