import datetime
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect # add render to import statement, add redirect to import statement
from django.http import JsonResponse

# Create your views here.

def home(request):
    return redirect("/time_display")


# def show_time(request):
#     context = {
#     	"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request, "index.html", context)

#BONUS
def show_time(request):
    now = datetime.datetime.now() # date et heure actuelles.
    formatted_date_time = now.strftime("%b %d %Y %I:%M %p")
    context = {
        "time": formatted_date_time,  
    }
    return render(request, "index.html", context)






