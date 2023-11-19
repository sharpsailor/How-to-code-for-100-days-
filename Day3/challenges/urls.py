from django.urls import path
from . import views # . iis used for root folder in django
urlpatterns = [
    path("",views.index),
	path("<int:month>",views.monthly_challenges_by_number),
	path("<str:month>",views.monthly_challenge, name ="month-challenge")
] # This is Known as The URL Config
