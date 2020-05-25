from django.contrib import admin
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.earningsSummary,name="earningsSummary"),
    path('earnings',views.earningsSummary,name="earningsSummary"),
    path('earning/<int:pk>',views.EaerningsUpdate.as_view(),name='earningsUpdate'),
    path('earnings/list',views.earningsList,name="earningsList"),
    path('earning/delete/<int:id>',views.earning_delete_view,name="earning_delete_view"),
    path('add/earnings',views.EarningsCreateView.as_view(),name='add_earnings'),
    path('add/expenses',views.ExpensesCreateView.as_view(),name='add_expenses'),
    path('expenses/list',views.expensesList,name="expensesList"),
    path('expense/<int:pk>',views.ExpensesUpdate.as_view(),name='expensesUpdate'),
    path('expense/delete/<int:id>',views.expense_delete_view,name="expense_delete_view"),
    path('reserve',views.reserveSummary,name="reserveSummary"),
    path('add/reserve/',views.ReserveCreateView.as_view(),name='add_reserve'),
    path('reserve/<int:pk>', views.ReserveUpdate.as_view(), name='ReserveUpdate'),
    path('reserve/delete/<int:id>', views.reserve_delete_view, name='reserve_delete_view'),
    path('roomst',views.roomsTransSummary, name="roomsTransactions"),
    path('add/roomt',views.RoomTCreateView.as_view(),name='add_room_transaction'),
    path('add/all-rent/roomt',views.RoomAllTCreateView.as_view(),name='add_rent-all_room_transaction'),
    path('roomst/list',views.roomsTransList,name="roomsTransList"),
    path('roomt/<int:pk>',views.RoomTranUpdate.as_view(),name="RoomTranUpdate"),
    path('roomt/delete/<int:id>',views.roomTransaction_delete_view,name="roomTransaction_delete_view"),
    path('roomsi',views.roomsInfoSummary,name="roomsInformation"),
    path('roomi/<int:pk>',views.RoomInfoUpdate.as_view(),name="RoomInfoUpdate"),
    path('add/roomi',views.RoomICreateView.as_view(),name='add_room_information'),
]
