#!/usr/bin/env python3
# This is a fake file to test the regex list
import os
import sys

# Here are things that should match, but be filtered out
URL = 'https://root:changeme@host:8080/otherthings'
some_password = "admin123"

# The following items should be found and reported
URL = 'https://root:F1ndM3USec@host:8080/goodthings'
REDIS = 'redis://redis:sUperSecRets@4.4.4.4:6379/#channel'
DB = "postgres://someuser:572132e287e97@somehost:381/somedatabase"
euuid = '123486f633883eb6f572132e287e9792aefd76089526a43938a3bccfad5b262c'
some_password = 'sUperSecRets!'
someother_password = "sUper2SecRets!"
somemore_password="sUper3SecRets!"
somemores_password='sUper4SecRets!'
yet_password = morethings_here #just a test
secret_sauce = 'Sp1cyP@ss1'
my_secret_token= "Sp1cyP@ss2"

# XML passwords (this might fail since not an XML file
<password>F0unDinXML</password>
<junk><password>F0unDin2XML</password></junk>
<more_password>Als0F0unDinXML</more_password>

# More things in other formats
Data Source=myServerAddress;location=myDataBase;User ID=myUsername;password=mySecRetsd;timeout=1000;
