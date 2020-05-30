from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.users_list,name="users_list"),
   # url(r'^(?P<pk>\d+)/$',views.users_detail,name="users_detail"),#here the integer value is saved in the variable named pk.
    url(r'^students/$',views.students_list,name="students_list"),
    url(r'^insert/$',views.insert_students,name="insert_students"),
    url(r'^delete/$',views.taskDelete,name="taskDelete"),
    url(r'^update/$',views.taskUpdate,name="taskUpdate"),


    
]
