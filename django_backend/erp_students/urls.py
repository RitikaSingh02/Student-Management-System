from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.users_list,name="users_list"),
   # url(r'^(?P<pk>\d+)/$',views.users_detail,name="users_detail"),#here the integer value is saved in the variable named pk.
    url(r'^teacher_login/$',views.teacher_login,name="teacher_login"),
    url(r'^student_login/$',views.student_login,name="student_login"),
    url(r'^students/$',views.students_list,name="students_list"),
    url(r'^insert/$',views.insert_students,name="insert_students"),
    url(r'^delete/$',views.taskDelete,name="taskDelete"),
    url(r'^update/$',views.taskUpdate,name="taskUpdate"),
    url(r'^ans_query/$',views.ansquery,name="ansquery"),
    url(r'^rejection/$',views.query_reject,name="query_reject"),
    url(r'^students_view/$',views.student_view,name="student_view"),
    url(r'^approval/$',views.query_approve,name="query_approve"),
    url(r'^change_password/$',views.change_pass,name="change_pass"),  
    url(r'^query_update/$',views.query_update,name="query_update"),
    url(r'^query_raisal/$',views.query_raise,name="query_raise"),
]