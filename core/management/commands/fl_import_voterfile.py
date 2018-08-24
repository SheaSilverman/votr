from django.core.management.base import BaseCommand, CommandError
from core.models import Voter, VoterException
import csv
import re

class Command(BaseCommand):
    help = 'Imports Voter Information CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)


    def handle(self, *args, **options):
        for csv_path in options['csv_path']:
            line = 0
            for row in getstuff(csv_path):
                if row[0] != 'County': # Ignore the header row, import everything else
                    # print row[4]
                    # print str(row[34]) + str(row[35]) + str(row[36])
                    # print row[37]
                    phone = str(str(row[34]) + str(row[35]) + str(row[36]))
                    email = row[37]
                    print "=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-"
                    print "phone", phone
                    print type(phone)
                    print "email", email
                    try:
                        obj, created = Voter.objects.update_or_create(

                            county = row[0],
                            voterID = row[1],

                            first_name = row[4],
                            last_name = row[2],
                            middle_name = row[5],
                            suffix = row[3],
                            exempt = row[6],


                            address1 = re.sub(' +', ' ',row[7]),
                            address2 = re.sub(' +', ' ',row[8]),
                            city = row[9],
                            state = row[10],
                            zipcode = row[11],

                            mailing_address1 = row[12],
                            mailing_address2 = row[13], 
                            mailing_address3 = row[14],
                            mailing_city = row[15],
                            mailing_state = row[16],
                            mailing_zipcode = row[17],
                            mailing_country = row[18],

                            gender = row[19],
                            race = row[20],
                            dob = row[21],
                            registration = row[22],
                            party = row[23],

                            precinct = row[24],
                            group = row[25],
                            split = row[26],
                            extra_suffix = row[27],
                            status = row[28],

                            congress = row[29],
                            state_house = row[30],
                            state_senate =row[31],
                            county_commission = row[32],
                            school_board= row[33],

                            phone = str(str(row[34]) + str(row[35]) + str(row[36])),
                            email = row[37]




                        )
                    except Exception, e:
                        obj, created = VoterException.objects.update_or_create(
                            county = row[0],
                            voterID = row[1]
                        )
                        print "Exception Occured - %s %s" % (row[1], row[2])
                        import sys, traceback
                        print traceback.print_exc()
                        #print str(e)

                    # voter.latitude = row[38]
                    # voter.longitude = row[39]
                    #voters.append(voter)
                    #voter.save()
                    
                    line +=1
                    if line % 1000 == 0:
                        print line


            #Voter.objects.bulk_create(voters)

def getstuff(filename):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in datareader:
            yield row