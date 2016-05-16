from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from models import Voter

from django_datatables_view.base_datatable_view import BaseDatatableView


# Create your views here.
def index(request):
    #return HttpResponse("Hi")
    return render(request, 'base.html')

def map(request):
    #return HttpResponse("Hi")
    return render(request, 'map2.html')

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

class VoterJson(BaseDatatableView):
    model = Voter
    columns = ['voterID', 'first_name', 'last_name',  'suffix', 'exempt',
     'address1', 'address2', 'city', 'zipcode',  'gender',  
     'party', 'status', 'email', 'phone', 'signature']
     
    order_columns = ['voterID', 'first_name', 'last_name',  'suffix', 'exempt',
     'address1', 'address2', 'city', 'zipcode',  'gender',  
     'party', 'status', 'email', 'phone', 'signature']

@csrf_exempt
def voter_signature(request):
    try:
        voteID = int(request.POST.get('voteID'))
        checked = bool(request.POST.get('checked'))
    except:
        return HttpResponse("Parameters not formatted correctly")
    
    try:
        voter = Voter.objects.get(voterID=voteID)
        print voter, voteID, checked
        voter.signature = checked
        voter.save()
    except:
        return HttpResponse("Unable to update voter")

    return HttpResponse("ok")

@csrf_exempt
def voter_map(request):
    print "hellO"
    print request.POST
    try:
        neLAT = float(request.POST.get("neLAT"))
        seLAT = float(request.POST.get("seLAT"))
        neLNG = float(request.POST.get("neLNG"))
        swLNG = float(request.POST.get("swLNG"))

    except:
        return HttpResponse("Parameters not formatted correctly")
    
    try:
        voters = Voter.objects.filter(latitude__lt=neLAT, latitude__gt=seLAT, longitude__lt=neLNG, longitude__gt=swLNG)
        data = serializers.serialize("json", voters)
        print "got data, sending"
        return HttpResponse(data, content_type='application/json')
    except:
        return HttpResponse("Unable to grab voter")

    return HttpResponse("ok")