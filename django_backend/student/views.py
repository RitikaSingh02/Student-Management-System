from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from rest_framework.parsers import JSONParser
from . models import users
from . models import students
from . serializers import usersserializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import json

@csrf_exempt
def users_list(request):
    if request.method=='GET':#get sends the data in key value  format
        user=users.objects.all()
        serializer=usersserializers(user,many=True)#many=True means that the query set contains many items so u need to serialise them
        return JsonResponse(serializer.data,safe=False)#If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed). 
        #If safe is True and a non-dict object is passed as the first argument, a TypeError will be raised.
        #serializer.data:returns an ordered dictionary

    
    elif request.method=='POST':
        USER_NAME=request.POST.get('USER_NAME',False)
        PASSWORD=request.POST.get('PASSWORD',False)
        USERTYPE=request.POST.get('USERTYPE',False)
        data = JSONParser().parse(request)
        # print(data['USER_NAME'])
        all_users=users.objects.raw("select * from student_users")
        if(data['USERTYPE']=='S'):
            id_input=users.objects.raw('''select * from student_users where USER_NAME=%s and PASSWORD=%s''',[data['USER_NAME'],data['PASSWORD']])
            num_results = users.objects.filter(USER_NAME=data['USER_NAME'],PASSWORD=data['PASSWORD']).count()
            if(num_results==0):
                data="wrong credentials"
                return JsonResponse(data,safe=False)
            else:
                return JsonResponse(data,safe=False) 
                        
                
        elif(data['USERTYPE']=='T'):
            id_input=users.objects.raw('''select * from student_users where USER_NAME=%s and PASSWORD=%s''',[data['USER_NAME'],data['PASSWORD']])
            num_results = users.objects.filter(USER_NAME=data['USER_NAME'],PASSWORD=data['PASSWORD']).count()
            if(num_results==0):
                data="wrong credentials"
                return JsonResponse(data,safe=False) 
            else:        
                return JsonResponse(data,safe=False)
                def teacher(request):
                    return render(request,'http://localhost/files/backend_faculty.html',{'all_users': all_users})
        else:
            data="wrong credentials"
            return JsonResponse(data,safe =False)

 

@csrf_exempt
def students_list(request):
    if request.method=='GET':#get sends the data in key value  format
        user=users.objects.raw("select * from student_users where USERTYPE='S'")
        serializer=usersserializers(user,many=True)#many=True means that the query set contains many items so u need to serialise them
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def insert_students(request):

    if request.method=='POST':
        print(json.loads(request.body))
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        USERTYPE='S'
        father_name=data['father_name']
        email=data['email']
        branch=data['branch']
        phone_no=data['phone_no']
        num_results = users.objects.filter(USER_NAME=USER_NAME).count()
        num_results1 = students.objects.filter(email=email).count()
        num_results2 = students.objects.filter(phone_no=phone_no).count()
        print(num_results)
        if(num_results==0):
            if(num_results1==0 and num_results2==0):
                print("#")
                info=users(USER_NAME=USER_NAME,USERTYPE=USERTYPE)
                print(info)
                info.save()
                detail=students(USER_NAME=USER_NAME,father_name=father_name,email=email,branch=branch,phone_no=phone_no)
                detail.save()
                data="Student inserted"
                print("%")
                return JsonResponse(data,safe=False)
            else:
                if(num_results1!=0 and num_results2!=0):
                    data="Duplicate entry for email and phone no"
                    return JsonResponse(data,safe=False)
                else:
                    if(num_results1!=0):
                        data="Duplicate entry for email"
                        return JsonResponse(data,safe=False)
                    if(num_results2!=0):
                        data="Duplicate entry for phone no"
                        return JsonResponse(data,safe=False)
        else:
            data="Student already exists"
            return JsonResponse(data,safe=False)
@csrf_exempt

def taskDelete(request):
    print(json.loads(request.body))
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    print(USER_NAME)
    users.objects.filter(USER_NAME=USER_NAME).delete()
    students.objects.filter(USER_NAME=USER_NAME).delete()

    return JsonResponse('Item succsesfully delete!',safe=False)


@csrf_exempt

def taskUpdate(request):
    print(json.loads(request.body))
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    USERTYPE='S'
    father_name=data['father_name']
    email=data['email']
    branch=data['branch']
    phone_no=data['phone_no']
    
    students.objects.filter(USER_NAME=USER_NAME).update(father_name=father_name,email=email,branch=branch,phone_no=phone_no)

    return JsonResponse("success",safe=False)


#You need to call is_valid during deserialization process before write data to DB.
# is_valid perform validation of input data and confirm that this data contain all required fields and all fields have correct types. 
# If validation process succeded is_valid set validated_data dictionary which is used for creation or updating data in DB.

#so in jsonResponse a list of many dictionaries is given as an output.