from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name="stu_index"),     # stu_index = 学生首页
]
