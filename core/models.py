from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Party(models.Model):
	name = models.CharField(max_length=200)

class Voter(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	street1 = models.CharField(max_length=200)
	street2 = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=200)
	state_house = models.IntegerField(default=0)
	state_senate = models.IntegerField(default=0)
	us_house = models.IntegerField(default=0)
	us_senate = models.IntegerField(default=0)
	school_board= models.IntegerField(default=0)
	active = models.IntegerField(default=0)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	party = models.ForeignKey(Party)
	latitude = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)



class Account(models.Model):
	name = models.CharField(max_length=200)
 
class AccountVoter(models.Model):
	voter = models.ForeignKey(Voter)
	signature = models.IntegerField(default=0)
	knocked = models.IntegerField(default=0)
	account = models.ForeignKey(Account)


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)