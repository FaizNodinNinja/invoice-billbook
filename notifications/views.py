from django.shortcuts import render

# Create your views here.

def notification_list(request):

    return render(request, 'notification/notification_list.html', )