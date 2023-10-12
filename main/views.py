from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def add_Employee_view(request):
    employye = Employee.objects.all()
    ser = EmployeeSerializers(employye, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_Employee_by_name(request):
    name = request.GET.get('name')
    employees = Employee.objects.filter(name__icontains=name)
    ser =  EmployeeSerializers(employees, many=True)
    return Response(ser.data)


@api_view(['GET'])
def add_Departament_view(request):
    departament = Departament.objects.all()
    ser = DepartamentSerializers(departament,many=True)
    return Response(ser.data)


@api_view(['GET'])
def add_Room_view(request):
    room = Room.objects.all()
    ser = RoomSerializers(room,many=True)
    return Response(ser.data)


@api_view(['GET'])
def Room_status_view(request):
    rooms = Room.objects.all()
    ser = RoomSerializers(rooms, many=True)
    room_data = ser.data
    for room in room_data:
        status = "Band" if room['is_booked'] else "Bo'sh"
        room.update({
            "status": status
        })
    return Response(ser.data)

@api_view(['GET'])
def filter_Room_by_name(request):
    name = request.GET.get('name')
    rooms = Room.objects.filter(name__icontains=name)
    ser =  RoomSerializers(rooms, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Bemor_view(request):
    bemor = Bemor.objects.all()
    ser = BemorSerializers(bemor,many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_Bemor_by_name(request):
    name = request.GET.get('name')
    bemor = Bemor.objects.filter(name__icontains=name)
    ser = BemorSerializers(bemor, many=True)
    return Response(ser.data)


@api_view(['POST'])
def calculate_bemor_view(request, pk):
    bemor = Bemor.objects.get(pk=pk)
    toatal = bemor.room.price*bemor.day
    cassa = Cassa.objects.get(pk=1)
    cassa.balance+=toatal
    cassa.save()
    create_bemor_calculator = Bemor_tolov.objects.create(
        bemor=bemor.pk,
        total_price=toatal,
    )

    ser = BemorSerializers(create_bemor_calculator)
    return Response(ser.data)


@api_view(['GET'])
def Cassa_view(request):
    cassa = Cassa.objects.all()
    ser = CassaSerializers(cassa,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_cassa_balance(request):
    cassa = Cassa.objects.first()
    ser= {
        "balance": cassa.balance,
        "income": cassa.income,
        "expense": cassa.expense,
    }
    return Response(ser)




@api_view(['GET'])
def total_expense(request):
    cassa = Cassa.objects.first()
    money = request.GET.get('money')
    cassa.balance -= money
    cassa.expense+= money
    ser = {'total_income': cassa.expense}
    return Response(ser)


@api_view(['GET'])
def total_income(request):
    cassa = Cassa.objects.first()
    money = request.GET.get('money')
    cassa.balance += money
    cassa.expense-= money
    ser = {'total_income': cassa.income}
    return Response(ser)
