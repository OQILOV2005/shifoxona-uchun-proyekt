from django.urls import path
from . import views


urlpatterns =[
    path('employee/', views.add_Employee_view),
    path('filters-employee/', views. filter_Employee_by_name),
    path('add-departament/', views. add_Departament_view),
    path('add-room/', views. add_Room_view),
    path('room-status/', views. Room_status_view),
    path('filters-room/', views. filter_Room_by_name),
    path('add-bemor/', views. Bemor_view),
    path('filters-bemor/', views. filter_Bemor_by_name),
    path('calculate-bemor/<int:pk>/', views. calculate_bemor_view),
    path(' Cassa/', views. Cassa_view),
    path('get-cassa-balance/', views.get_cassa_balance),
    path('total-income/', views.total_income),
    path('total-expense/', views.total_expense),
]