from django.urls import path
from .views import homepage, me, contact

urlpatterns = [
   path('', homepage),
   path('me/', me),
   path('contact/', contact),
]