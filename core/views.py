from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.views.generic import ListView
from django.db.models import Q
from models import Voter

from django_datatables_view.base_datatable_view import BaseDatatableView


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

def voter_json(request):
    start = request.GET.get('start')
    length = request.GET.get('length')

    voter_list = Voter.objects.all()[start:length]
    voter_data = serializers.serialize("json", voter_list)
    print voter_data
    return JsonResponse(voter_data, safe=False)

class VoterJson(BaseDatatableView):
    model = Voter
    columns = ['county', 'voterID', 'first_name', 'last_name', 'middle_name', 'suffix', 'exempt',
     'address1', 'address2', 'city', 'state', 'zipcode', 'mailing_address1', 'mailing_address2', 'mailing_city', 'mailing_state',
     'mailing_zipcode', 'mailing_country', 'gender', 'race', 'dob', 'registration', 'party',
     'precinct', 'group', 'split', 'extra_suffix', 'status', 'state_house', 'state_senate', 'congress', 'school_board', 
     'email', 'phone', 'latitude', 'longitude']
    order_columns = ['county', 'voterID', 'first_name', 'last_name', 'middle_name', 'suffix', 'exempt',
     'address1', 'address2', 'city', 'state', 'zipcode', 'mailing_address1', 'mailing_address2', 'mailing_city', 'mailing_state',
     'mailing_zipcode', 'mailing_country', 'gender', 'race', 'dob', 'registration', 'party',
     'precinct', 'group', 'split', 'extra_suffix', 'status', 'state_house', 'state_senate', 'congress', 'school_board', 
     'email', 'phone', 'latitude', 'longitude']
