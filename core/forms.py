from django import forms

class SearchForm(forms.Form):
    voter_first_name = forms.CharField(label='Name', max_length=100, required=False)
    voter_last_name = forms.CharField(label='Name', max_length=100, required=False)
    voter_party = forms.CharField(label='Party', max_length=100, required=False)
    voter_address1 = forms.CharField(label='Address1', max_length=100, required=False)

class SearchForm1(forms.Form):
    query = forms.CharField(label='Name', max_length=100, required=False)
