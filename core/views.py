from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
from models import Voter

# Create your views here.
def index(request):
    #return HttpResponse("Hi")
    return render(request, 'base.html')


def voter(request):
    voter_list = Voter.objects.all()
    
    paginator = Paginator(voter_list, 500) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        voters = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        voters = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        voters = paginator.page(paginator.num_pages)

    return render(request, 'voter_list.html', {'voters': voters})

# class VoterList(ListView):
#     model = Voter
