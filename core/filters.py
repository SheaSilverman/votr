# from django.contrib.auth.models import User
from models import Voter
import django_filters

# class UserFilter(django_filters.FilterSet):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', ]

class VoterFilter(django_filters.FilterSet):
    class Meta:
        model = Voter
        # date_between = django_filters.DateFromToRangeFilter(name='dob',
        #                                                      label='Date (Between)')
        fields = ['first_name', 'last_name', 'dob']