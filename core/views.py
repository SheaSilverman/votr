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

def cluster(request):
    return render(request, 'clustermap.html')

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
     'party', 'status', 'email', 'phone', 'latitude', 'longitude']
     
    order_columns = ['voterID', 'first_name', 'last_name',  'suffix', 'exempt',
     'address1', 'address2', 'city', 'zipcode',  'gender',  
     'party', 'status', 'email', 'phone']

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
    print "hello"
    print request.POST
    try:
        east = float(request.POST.get("east"))
        west = float(request.POST.get("west"))
        north = float(request.POST.get("north"))
        south = float(request.POST.get("south"))

    except:
        return HttpResponse("Parameters not formatted correctly")
    
    try:
        voters = Voter.objects.filter(latitude__lt=east, latitude__gt=west, longitude__lt=north, longitude__gt=south)
        data = serializers.serialize("json", voters)
        print "got data, sending"
        return HttpResponse(data, content_type='application/json')
    except:
        return HttpResponse("Unable to grab voter")

    return HttpResponse("ok")

# select * from core_voter where latitude >=-81.24831676483156  and latitude <=-81.21939182281496  and longitude >=28.59015539969054  and longitude <= 28.597691623705916 ;
# console.log("select * from core_voter where latitude >=" + map.getBounds().getWest() + "  and latitude <=" + map.getBounds().getEast() + "  and longitude >=" + map.getBounds().getSouth() + "  and longitude <= " + map.getBounds().getNorth() + " ;");

#           console.log(map.getBounds().getEast());
#           console.log(map.getBounds().getWest());
#           console.log(map.getBounds().getNorth());
#           console.log(map.getBounds().getSouth());