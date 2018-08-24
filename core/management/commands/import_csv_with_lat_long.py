from django.core.management.base import BaseCommand, CommandError
from core.models import Voter
import csv

class Command(BaseCommand):
    help = 'Imports Voter Information CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_path in options['csv_path']:
            dataReader = csv.reader(open(csv_path), delimiter=',', quotechar='"')
            voters = []
            for row in dataReader:
                if row[0] != 'County': # Ignore the header row, import everything else
                    voter = Voter()

                    voter.county = row[0]
                    voter.voterID = row[1]

                    voter.first_name = row[4]
                    voter.last_name = row[2]
                    voter.middle_name = row[5]
                    voter.suffix = row[3]
                    voter.exempt = row[6]


                    voter.address1 = row[7]
                    voter.address2 = row[8]
                    voter.city = row[9]
                    voter.state = row[10]
                    voter.zipcode = row[11]

                    voter.mailing_address1 = row[12]
                    voter.mailing_address2 = row[13]
                    voter.mailing_address2 = row[14]
                    voter.mailing_city = row[15]
                    voter.mailing_state = row[16]
                    voter.mailing_zipcode = row[17]
                    voter.mailing_country = row[18]

                    voter.gender = row[19]
                    voter.race = row[20]
                    voter.dob = row[21]
                    voter.registration = row[22]
                    voter.party = row[23]

                    voter.precinct = row[24]
                    voter.group = row[25]
                    voter.split = row[26]
                    voter.extra_suffix = row[28]
                    voter.status = row[29]

                    voter.state_house = row[30]
                    voter.state_senate =row[31]
                    voter.congress = row[32]
                    voter.school_board= row[33]

                    voter.phone = row[34] + row[35] + row[36]
                    voter.email = row[37]

                    voter.latitude = row[38]
                    voter.longitude = row[39]
                    voters.append(voter)
            Voter.objects.bulk_create(voters)