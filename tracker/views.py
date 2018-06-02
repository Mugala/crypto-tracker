from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . request import all_currencies,all_news
from .models import Profile, Currency,Currency_details,Article
from .forms import NewsLetterForm, User_details
from django.contrib.auth.decorators import login_required

# Create your views here.


def welcome(request):
    return render (request, "welcome.html")




@login_required(login_url='/accounts/login/')
def crypto(request):
    currency = all_currencies(id)


    return render (request, "dashboard/crypto.html",{'currency':currency})



def news(request):
    articles = all_news()


    return render (request, "dashboard/news.html",{'articles':articles})





def user_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = User_details(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect("my_profile")
    else:
        form = User_details()
    return render(request, 'dashboard/user_profile.html', {"form": form})

def my_profile(request):
    user_details = Profile.user_details()
    
    return render(request, 'dashboard/user_account.html', {"user_details": user_details,})


def search_results(request):

    if 'currency' in request.GET and request.GET["currency"]:
        search_term = request.GET.get("currency")
        results = all_currencies(search_term)
        message = f"{search_term}"

        return render(request, 'dashboard/search.html', {"message": message, "currencies": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'dashboard/search.html', {"message": message})
  

