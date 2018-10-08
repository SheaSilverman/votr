# Votr
### About
My name is Shea Silverman, and I am running for Florida's House of 
Representatives in District 49.  I am running as/with no party 
affiliation. This tool is to help keep track of your district voters, 
your volunteers, your signatures, and your donations.
### Configuration

 ``` 
 virtualenv ENV 
 source ENV/bin/activate 
 git clone https://github.com/sheasilverman/votr 
 cd votr
 pip install -r requirements.txt 
 python manage.py migrate 
 python manage.py import_csv <district file> 
 python manage.py runserver 
```

##2018

```
 virtualenv ENV 
 source ENV/bin/activate 
 git clone https://github.com/sheasilverman/votr 
 cd votr
 pip install -r requirements.txt 
 python manage.py migrate 
 python manage.py fl_import_voterfile <voterfile.csv>
```

You then need to run a geocoder on your voter file to set get the most of this running.  
I use pelias+openaddress.  
Once that is installed you can run:

```
python manage.py fl_geocode
```

Finally run the server with:
```
 python manage.py runserver 
```

### Issues
This is a VERY early work in progress.  Not ready for production use.
