from django.core.management.base import BaseCommand, CommandError
from core.models import Voter, VoterException
import csv
import requests

ngrok_url = "http://127.0.0.1/v1/search?text="


class Command(BaseCommand):
    help = 'Gets distinct addresses without lat/long and then geocodes them.'


    def handle(self, *args, **options):
        addresses = Voter.objects.raw("SELECT distinct address1, address2, city, state, zipcode FROM core_voter where latitude is null and longitude is null")
        for a in addresses:
            try:
                latitude, longitude = get_latlong(a.address1, a.address2, a.city, a.zipcode)

                voters = Voter.objects.filter(address1=address1, address2=address2, city=city, zipcode=zipcode)
                for v in voters:
                    v.longitude = longitude
                    v.latitude = latitude
                    v.save()
            except:
                print "Exception Occured"
                import sys, traceback
                print traceback.print_exc()



def get_latlong(address1, address2, city, zipcode):
    print address1
    try:
        url = "%s%s %s %s %s" % (ngrok_url, address1, address2, city, zipcode)
        r = requests.get(url)
        parsed_json = r.json()
        longitude = parsed_json['features'][0]['geometry']['coordinates'][0]
        latitude = parsed_json['features'][0]['geometry']['coordinates'][1]
        return longitude, latitude
    except:
        print "Exception Occured"
        print id
        import sys, traceback
        print traceback.print_exc()
