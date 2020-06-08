from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from . models import users,students,queries
import json


def users_list(request):
    if request.method=='GET':
        #get sends the data in key value  format
        user=users.objects.filter(status="Active").values()
        
        return JsonResponse( list(user),safe=False)

def teacher_login(request):
    if(request.method=="POST"):
        print(json.loads(request.body))
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        PASSWORD=data['PASSWORD']
        num=users.objects.filter(USER_NAME=USER_NAME,PASSWORD=PASSWORD,USERTYPE="T").count()
        print(num)
        if(num==1):
            print("#")
            return JsonResponse("logged in",safe=False)

        else:
            return JsonResponse("wrong credentials",safe=False)
    

def student_login(request):
    if(request.method=="POST"):
        print(json.loads(request.body))
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        PASSWORD=data['PASSWORD']
        num=users.objects.filter(USER_NAME=USER_NAME,PASSWORD=PASSWORD,USERTYPE='S').count()
        if(num==1):
            #print(str(data['USER_NAME']))
            user=users.objects.filter(USER_NAME=USER_NAME,PASSWORD=PASSWORD,USERTYPE='S').values()
            #print(list(user))
            return JsonResponse(list(user),safe=False)
        else:
            return JsonResponse("wrong credentials",safe=False)
    


def students_list(request):
    if request.method=='GET':#get sends the data in key value  format
        users=students.objects.all().values()
        print(list(users))      
        return JsonResponse(list(users),safe=False)



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
        
        if(num_results==0):
            if(num_results1==0 and num_results2==0):
               # print("#")
                info=users(USER_NAME=USER_NAME,USERTYPE=USERTYPE)
               # print(info)
                info.save()
                detail=students(USER_NAME=USER_NAME,father_name=father_name,email=email,branch=branch,phone_no=phone_no)
                query_element=queries(USER_NAME=USER_NAME)
                query_element.save()
                detail.save()
                data="Student inserted"
               # print("%")
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


def taskDelete(request):
    print(json.loads(request.body))
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    print(USER_NAME)
    users.objects.filter(USER_NAME=USER_NAME).delete()
    students.objects.filter(USER_NAME=USER_NAME).delete()
    queries.objects.filter(USER_NAME=USER_NAME).delete()

    return JsonResponse('Item succsesfully delete!',safe=False)




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
    print("updated successfully")
    return JsonResponse("success updation",safe=False)

def query_raise(request):
    print(json.loads(request.body))
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    students.objects.filter(USER_NAME=USER_NAME).update(STATUS="PENDING")
    queries.objects.filter(USER_NAME=USER_NAME).update(STATUS="PENDING")
    return JsonResponse("QUERY HAS BEEN RAISED",safe=False)



def ansquery(request):

    if request.method=='GET':#get sends the data in key value  format
        query_element=queries.objects.filter(STATUS="PENDING").values()        
        print(list(query_element))      
        return JsonResponse(list(query_element),safe=False)
    
def query_reject(request):
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']    
    queries.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST REJECTED")
    students.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST REJECTED")
    return JsonResponse("rejected",safe=False)

def query_approve(request):
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    queries.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST APPROVED")
    students.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST APPROVED")
    return JsonResponse("approved",safe=False)


def student_view(request):
    if request.method=='POST':#get sends the data in key value  format
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        users=students.objects.filter(USER_NAME=USER_NAME).values()
        print(list(users))      
        return JsonResponse(list(users),safe=False)

def change_pass(request):
    if request.method=="POST":
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        PASSWORD=data['PASSWORD']
        student=students.objects.filter(USER_NAME=USER_NAME).update(PASSWORD=PASSWORD)
        users1=users.objects.filter(USER_NAME=USER_NAME).update(PASSWORD=PASSWORD)
              
        return JsonResponse("password updated successfully",safe=False)

def query_update(request):
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    father_name=data['father_name']
    email=data['email']
    branch=data['branch']
    phone_no=data['phone_no']
    
    num=students.objects.filter(USER_NAME=USER_NAME,STATUS='REQUEST APPROVED').count()
    if(num!=0):
        students.objects.filter(USER_NAME=USER_NAME,STATUS='REQUEST APPROVED').update(father_name=father_name,email=email,branch=branch,phone_no=phone_no)
        print("updated successfully")
        return JsonResponse("success updation",safe=False)
    else:
        return JsonResponse("YOUR REQUEST HAS NOT BEEN APPROVED YET ",safe=False)


    



#You need to call is_valid during deserialization process before write data to DB.
# is_valid perform validation of input data and confirm that this data contain all required fields and all fields have correct types. 
# If validation process succeded is_valid set validated_data dictionary which is used for creation or updating data in DB.

#so in jsonResponse a list of many dictionaries is given as an output.