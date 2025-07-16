from django.http import HttpResponse, HttpRequest
from django.views import View

class HomeView(View):
        
    def get(self, request: HttpRequest):
        return HttpResponse(f"Hola usuario,estas auntentificado? {request.user.is_authenticated}")