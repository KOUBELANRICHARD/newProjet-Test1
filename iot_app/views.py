from django.shortcuts import render
from .models import Client

def clients_view(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})
