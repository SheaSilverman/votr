from django.core.management.base import BaseCommand, CommandError
from core.models import Voter, VoterException
import csv
import requests

ngrok_url = "http://127.0.0.1/v1/search?text="


class Command(BaseCommand):
    help = 'Imports Voter Information CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)


    def handle(self, *args, **options):
        for csv_path in options['csv_path']:
            line = 0
            for row in get_csv_row(csv_path):
                if row[0] != 'address1': # Ignore the header row, import everything else
                    try:
                        #addr = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4]
                        address1 = row[0]
                        address2 = row[1]
                        city = row[2]
                        state = row[3]
                        zipcode = row[4]
                        latitude, longitude = get_latlong(address1, address2, city, state, zipcode)

                        voters = Voter.objects.filter(address1=address1, address2=address2, city=city, zipcode=zipcode)
                        for v in voters:
                            v.longitude = longitude
                            v.latitude = latitude
                            v.save()

                    except:
                        print "Exception Occured"
                        print id
                        import sys, traceback
                        print traceback.print_exc()

                    # voter.latitude = row[38]
                    # voter.longitude = row[39]
                    #voters.append(voter)
                    #voter.save()
                    
                    line +=1
                    print line


def get_latlong(address1, address2, city,  zipcode):
    print address1
    try:
        url = "%s%s %s %s %s" % (ngrok_url, address1, address2,  state, zipcode)
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

def get_csv_row(filename):
    #SELECT distinct address1, address2, city, state, zipcode
    #  FROM core_voter;
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in datareader:
            yield row