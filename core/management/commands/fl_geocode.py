from django.core.management.base import BaseCommand, CommandError
from core.models import Voter, VoterException, VoterLatLongException
import requests

ngrok_url = "http://454fa8e4.ngrok.io/v1/search?text="

class Command(BaseCommand):
    help = 'Adds Lat/Long to VoterFile'

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_path', nargs='+', type=str)


    def handle(self, *args, **options):
        count = Voter.objects.all().count()
        print count

        # count = 10
        # print count
        i = 1
        while i < count:
            print(i)
            try:
                v = Voter.objects.get(pk=i)
                url = "%s%s %s %s %s %s" % (ngrok_url, v.address1, v.address2, v.city, v.state, v.zipcode)
                print(url)
                r = requests.get(url)
                parsed_json = r.json()
                longitude = parsed_json['features'][0]['geometry']['coordinates'][0]
                latitude = parsed_json['features'][0]['geometry']['coordinates'][1]
                v.longitude = longitude
                v.latitude = latitude
                v.save()
            except:
                print "Exception Occured"
                print i
                import sys, traceback
                print traceback.print_exc()
            i += 1
