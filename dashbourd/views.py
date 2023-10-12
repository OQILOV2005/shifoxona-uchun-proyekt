from main.models import  Employee,Departament,Room,Bemor
from main.serializers import *
from rest_framework.decorators import api_view
from  rest_framework.response import Response

@api_view(['POST'])
def create_employee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        photo = request.POST.getlist('photo')
        direction = request.POST.get('direction')
        experience = request.POST.get('experience')
        salary = request.POST.get('salary')
        age = request.POST.get('age')
        room = request.POST.get('room')
        section = request.POST.get('section')
        new_employee = Employee.objects.create(
            name = name,
            phone = phone,
            photo = photo,
            direction = direction,
            experience = experience,
            salary = salary,
            age = age,
            room = room,
            section = section,
        )
        for i in photo:
            new_employee.photo.add(i)
            new_employee.save()
        ser = EmployeeSerializers(new_employee)
        return Response(ser.data)



@api_view(['PUT'])
def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    photo = request.POST.getlist('photo')
    direction = request.POST.get('direction')
    experience = request.POST.get('experience')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    room = request.POST.get('room')
    section = request.POST.get('section')

    employee.name=name
    employee.phone=phone
    employee.photo=photo
    employee.direction=direction
    employee.experience=experience
    employee.salary=salary
    employee.age=age
    employee.room=room
    employee.section=section
    if photo is not None:
        employee.save()
    ser = EmployeeSerializers(employee)
    return Response(ser.data)


@api_view(['POST'])
def create_departament(request):
    if request.method == "POST":
       name = request.POST.get('name')
       descriptioon  = request.POST.get(' descriptioon ')
       new_departament = Departament.objects.create(
           name = name,
       descriptioon = descriptioon,
       )
       new_departament.save()
       ser = DepartamentSerializers(new_departament)
       return Response(ser.data)


@api_view(['PUT'])
def update_departament(request,pk):
       departament = Departament.objects.get(pk=pk)
       name = request.POST.get('name')
       descriptioon  = request.POST.get(' descriptioon ')
       departament.name = name
       departament.descriptioon = descriptioon

       departament.save()
       ser = DepartamentSerializers(departament)
       return Response(ser.data)


@api_view(['POST'])
def create_room(request):
    if request.method == "POST":
       name = request.POST.get('name')
       price  = request.POST.get(' price ')
       new_room = Room.objects.create(
           name = name,
           price = price
       )
       new_room.save()
       ser = RoomSerializers(new_room)
       return Response(ser.data)


@api_view(['PUT'])
def update_room(request,pk):
       room = Room.objects.get(pk=pk)
       name = request.POST.get('name')
       price  = request.POST.get(' price ')
       room.name = name
       room.price = price

       room.save()
       ser = RoomSerializers(room)
       return Response(ser.data)


@api_view(['POST'])
def create_bemor(request):
   if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        day = request.POST.get('day')
        room = request.POST.get('room')
        doktori = request.POST.get('doktori')
        new_bemor = Bemor.objects.create(
            name = name,
            age = age,
            phone = phone,
            day = day,
            room = room,
            doktori = doktori,
        )
        new_bemor.save()
        ser = BemorSerializers(new_bemor)
        return Response(ser.data)


@api_view(['PUT'])
def update_bemor(request,pk):
        bemor = Bemor.objects.get(pk=pk)
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        day = request.POST.get('day')
        room = request.POST.get('room')
        doktori = request.POST.get('doktori')
        bemor.name = name,
        bemor.age = age,
        bemor.phone = phone,
        bemor.day = day,
        bemor.room = room,
        bemor.doktori = doktori,

        bemor.save()
        ser = BemorSerializers(bemor)
        return Response(ser.data)




@api_view(["DELETE"])
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return Response({'message' : "Deleted"})

@api_view(["DELETE"])
def delete_employee(request, pk):
    departament = Departament.objects.get(pk=pk)
    departament.delete()
    return Response({'message' : "Deleted"})

@api_view(["DELETE"])
def delete_room(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    return Response({'message' : "Deleted"})


@api_view(["DELETE"])
def delete_bemor(request, pk):
    bemor = Bemor.objects.get(pk=pk)
    bemor.delete()
    return Response({'message' : "Deleted"})