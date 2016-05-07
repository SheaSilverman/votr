from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from models import Voter



# Create your views here.
def index(request):
	return HttpResponse("Hi")

def voter(request):
	voters = Voter.objects.all()
	context = {'voters': voters}
	return render(request, 'voter_list.html', context)



# class VoterList(ListView):
#     model = Voter