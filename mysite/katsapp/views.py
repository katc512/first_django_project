from django.http import JsonResponse

# Create your views here.

def index(request):
    data = {

   "Name" : "Katrina Coles",

    "Track" : "Backend(Python)",

    "Message" : "Is it even possible to have less than 100 tabs open at once?!"
    
    }

    return JsonResponse(data)