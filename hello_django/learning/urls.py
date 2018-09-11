from django.urls import path
from learning import views

urlpatterns = [
    path('', views.index, name="sales_index"),     # sales_index = 销售首页
    path('customer/', views.customer_list, name="customer_list"),     # sales_index = 销售首页
]
