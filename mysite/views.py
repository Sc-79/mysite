from django.http import HttpResponse
from django.shortcuts import render
 
def aboutUs(request):
    return HttpResponse("About Us Page")
def Course(request):
    return HttpResponse("my course")

def CourseDetails(request, courseid):
    return HttpResponse(f"{courseid} - Welcome to My Course")

#    def Home(request):
#         return render(request, "index.html")
# def Home(request):
#      data={
#         'title':'home page'
#      }
#     return render(request, "index.html",data)
def home(request):
    data = {
        'title': 'home page sourav',
        'name':'Sourav chongrey',
        'clist':['php', 'java','Django'],
        'numbers':[12,34,55,66,77,8,88,88,99,99],
        'student_details':[
            {'name':'sourav', 'phone':7001589285},
            {'name':'akash', 'phone':9609952986}
        ]
    }
    return render(request, "index.html", data)
