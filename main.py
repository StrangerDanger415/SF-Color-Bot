import requests
import time
import tweepy
import json
import pytz
from datetime import datetime


auth = tweepy.OAuthHandler("FCOFRfItfXNkMAXdV2qJnVWY0", "wXUEZNXxD0y3J6jTS9XXfpEkwh4V8O1if3CA8LBN1yxA8SY4IO")
auth.set_access_token("1348188829543395333-qCJaTtfjBHRYIItCCNlmLGidkpZmuo","BsKuKL60fpe1E4MoRmUI4JyH10nlgiiGjBaJCtSqEAuUO")

api = tweepy.API(auth)

s = requests.get('https://home.color.com/api/v1/sample_collection_appointments/availability?claim_token=26717ed0ee09e42721b5439ef1e7a44f2ad9&collection_site=Alemany%20Farmers%20Market')
r = requests.get('https://home.color.com/api/v1/sample_collection_appointments/availability?claim_token=26717ed0ee09e42721b5439ef1e7a44f2ad9&collection_site=Embarcadero')

r = r.json()
s = s.json()

while True:
    for e in r:
            if not r:
                break
            else:
                #Converting json result to datetime format
                start = datetime.fromisoformat(e['start'])
                end = datetime.fromisoformat(e['end'])
                #Converting UTC time to PDT
                start = start.astimezone(pytz.timezone("America/Los_Angeles"))
                end = end.astimezone(pytz.timezone("America/Los_Angeles"))
                api.update_status(f'Embarcadero Open Appts: {start:%Y-%m-%d %I:%M %p} to {end:%Y-%m-%d %I:%M %p}')
    for a in s:
            if not s:
                break
            else:
                #Converting json result to datetime format
                start1 = datetime.fromisoformat(a['start'])
                end1 = datetime.fromisoformat(a['end'])
                #Converting UTC time to PDT
                start1 = start1.astimezone(pytz.timezone("America/Los_Angeles"))
                end1 = end1.astimezone(pytz.timezone("America/Los_Angeles"))
                api.update_status(f'Alemany Open Appts: {start1:%Y-%m-%d %I:%M %p} to {end1:%Y-%m-%d %I:%M %p}')
    time.sleep(60)

