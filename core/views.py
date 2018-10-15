from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from models import Voter

from django_datatables_view.base_datatable_view import BaseDatatableView

from .filters import VoterFilter

# Create your views here.
def index(request):
    #return HttpResponse("Hi")
    return render(request, 'base.html')


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

    # def filter_queryset(self, qs):
    #     # use parameters passed in GET request to filter queryset

    #     # simple example:
    #     search = self.request.GET.get('search[value]', None)
    #     if search:
    #         qs = qs.filter(first_name__istartswith=search)

    #     # more advanced example using extra parameters
    #     # filter_customer = self.request.GET.get('customer', None)

    #     # if filter_customer:
    #     #     customer_parts = filter_customer.split(' ')
    #     #     qs_params = None
    #     #     for part in customer_parts:
    #     #         q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
    #     #         qs_params = qs_params | q if qs_params else q
    #     #     qs = qs.filter(qs_params)
    #     return qs

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
    # print "hello"
    # print request.POST
    try:
        east = float(request.POST.get("east"))
        west = float(request.POST.get("west"))
        north = float(request.POST.get("north"))
        south = float(request.POST.get("south"))

    except:
        return HttpResponse("Parameters not formatted correctly")
    
    try:
        voters = Voter.objects.filter(latitude__lt=east, latitude__gt=west, longitude__lt=north, longitude__gt=south)
        voter_filter = VoterFilter(request.POST, queryset=voters)
        #data = serializers.serialize("json", voters)
        data = serializers.serialize("json", voter_filter.qs)
        print(voter_filter)
        # print "got data, sending"
        return HttpResponse(data, content_type='application/json')
    except Exception as e:
        import traceback
        traceback.print_exc()
        print e
        return HttpResponse("Unable to grab voter")

    # return HttpResponse("ok")

# select * from core_voter where latitude >=-81.24831676483156  and latitude <=-81.21939182281496  and longitude >=28.59015539969054  and longitude <= 28.597691623705916 ;
# console.log("select * from core_voter where latitude >=" + map.getBounds().getWest() + "  and latitude <=" + map.getBounds().getEast() + "  and longitude >=" + map.getBounds().getSouth() + "  and longitude <= " + map.getBounds().getNorth() + " ;");

#           console.log(map.getBounds().getEast());
#           console.log(map.getBounds().getWest());
#           console.log(map.getBounds().getNorth());
#           console.log(map.getBounds().getSouth());




def search(request):
    voter_list = Voter.objects.all()
    voter_filter = VoterFilter(request.GET, queryset=voter_list)
    return render(request, 'user_list.html', {'filter': voter_filter})