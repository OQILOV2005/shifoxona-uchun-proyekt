from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField
class User(AbstractUser):
    phone  = models.CharField(max_length=13, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class  Employee(models.Model):
   name = models.CharField(max_length=30)
   phone = models.CharField(max_length=13, unique=True, validators=[
       RegexValidator(
           regex='^[\+]9{2}8{1}[0-9]{9}$',
           message='Invalid phone number',
           code='invalid_number'
       ), ])
   photo = models.ImageField(upload_to='Employee_image/',verbose_name='ishchi rasmi')
   direction = models.CharField(max_length=30,verbose_name='ish sohasi')
   experience = models.IntegerField(verbose_name='ish tajribasi')
   salary = models.IntegerField(verbose_name='ish haqi')
   age = models.IntegerField(verbose_name='yoshi')
   room = models.ForeignKey(to="Room", on_delete=models.CASCADE,verbose_name='xona')
   section = models.ForeignKey(to='Departament', on_delete=models.PROTECT,verbose_name='bolimi nomi')

   def __str__(self):
        return self.name


class Departament(models.Model):
    name = models.CharField(max_length=25,verbose_name='bolim nomi')
    descriptioon = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class Bemor(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    day = models.IntegerField(null=True,blank=True)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    doktori = models.ForeignKey(to=Employee, on_delete=models.PROTECT)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.bemor.name


class Bemor_tolov(models.Model):
    bemor = models.ForeignKey(to=Bemor, on_delete=models.PROTECT)
    total = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
          return self.bemor.name


class Cassa(models.Model):
    income = models.IntegerField(default=0)
    expense = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)





