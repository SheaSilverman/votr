from django.core.management.base import BaseCommand, CommandError
from core.models import Voter, VoterException, VoterLatLongException
import requests

from multiprocessing.pool import ThreadPool

ngrok_url = "http://127.0.0.1/v1/search?text="

class Command(BaseCommand):
    help = 'Adds Lat/Long to VoterFile'

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
        pool = ThreadPool(8)
        #pool.map(get_voter, xrange(Voter.objects.all().count()))
        # objects = Voter.objects.filter(latitude__isnull=True)
        # mylist = [obj.id for obj in objects]
        pool.map(get_voter, get_row())
 
def get_voter(id):
    print id
    try:
        v = Voter.objects.get(pk=id)
        url = "%s%s %s %s %s %s" % (ngrok_url, v.address1, v.address2, v.city, v.state, v.zipcode)
        r = requests.get(url)
        parsed_json = r.json()
        longitude = parsed_json['features'][0]['geometry']['coordinates'][0]
        latitude = parsed_json['features'][0]['geometry']['coordinates'][1]
        v.longitude = longitude
        v.latitude = latitude
        v.save()
    except:
        print "Exception Occured"
        print id
        import sys, traceback
        print traceback.print_exc()
     

def get_row():
    objects = Voter.objects.filter(latitude__isnull=True)
    for o in objects:
        yield o.id