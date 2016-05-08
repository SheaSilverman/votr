from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Party(models.Model):
	name = models.CharField(max_length=200)


	#Gender	Race	DOB	Registration	Party	Precinct	Group	Split	Suffix	Status	Congress	House	Senate	Commision	SchoolBoard	AreaCode	PhoneNumber	Extension	email	latitude	longitude

class Voter(models.Model):
	county = models.CharField(max_length=200)
	voterID = models.IntegerField(default=0)


	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	suffix = models.CharField(max_length=200)
	exempt = models.CharField(max_length=200)


	address1 = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=200)

	mailing_address1 = models.CharField(max_length=200)
	mailing_address2 = models.CharField(max_length=200)
	mailing_address2 = models.CharField(max_length=200)
	mailing_city = models.CharField(max_length=200)
	mailing_state = models.CharField(max_length=200)
	mailing_zipcode = models.CharField(max_length=200)
	mailing_country = models.CharField(max_length=200)

	gender = models.CharField(max_length=200)
	race = models.CharField(max_length=200)
	dob = models.CharField(max_length=200)
	registration = models.CharField(max_length=200)
	party = models.CharField(max_length=5)
	
	precinct = models.IntegerField(default=0)
	group = models.CharField(max_length=200)
	split = models.CharField(max_length=200)
	extra_suffix = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	
	state_house = models.IntegerField(default=0)
	state_senate = models.IntegerField(default=0)
	congress = models.IntegerField(default=0)
	school_board= models.IntegerField(default=0)

	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	#party = models.ForeignKey(Party)
	latitude = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



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