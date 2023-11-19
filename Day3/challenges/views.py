from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    list_items = ""
    months= list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path= reverse("month-challenge",args=[month])
        list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        reponse_data = f"<ul>{list_items}</ul"
    return HttpResponse(reponse_data)
monthly_challenges = {
    
    "january":"Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!" ,
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!" ,
    "june": "Learn Django for at least 20 minutes every day!" ,
    "july":"Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!" ,
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"    
}
def monthly_challenges_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month >len(months) | month<0:
        return HttpResponseNotFound("Hey enter a Valid Month")
    redirect_month = months[(month-1)]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /Challenge
     # Path for Urls is Month_challenge since any one can change so we have added it to the resverse Package which redirects to reversed path
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
#    2nd Alternative
    # months = {
    #     "january": "January",
    #     "february": "February",
    #     "march": "March",
    #     "april": "April",
    #     "may": "May",
    #     "june": "June",
    #     "july": "July",
    #     "august": "August",
    #     "september": "September",
    #     "october": "October",
    #     "november": "November",
    #     "december": "December"
    # }

    # Check if the month exists in the dictionary, if yes, set the challenge_text
    # challenge_text = months.get(month.lower())
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>" # String Interpolation is used to convert  strings to strings  in  the response    
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This Month is not a valid challenge</h1>")

    # return HttpResponse(challenge_text)
    # if challenge_text:
    #     return HttpResponse("This month is " + challenge_text)
    # else:
    #     return HttpResponseNotFound("This month is not a valid challenge")