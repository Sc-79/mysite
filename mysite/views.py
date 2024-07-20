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
        'title': 'home page sourav'
    }
    return render(request, "index.html", data)
