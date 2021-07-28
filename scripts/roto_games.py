import requests
import datetime

import os
from os import sys, path
import django

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fantasy_mlb.settings")
django.setup()

from general.models import *
from general.views import *
from general import html2text
from scripts.get_slate import get_slate


def get_games(data_source, data_source_id):
    slate_id = get_slate(data_source)
    url = 'https://www.rotowire.com/daily/tables/mlb/schedule.php' + \
          '?siteID={}&slateID={}'.format(data_source_id, slate_id)
    print (url)

    games = requests.get(url).json()
    if games:
        Game.objects.filter(data_source=data_source, lock_update=False).delete()

        fields = ['ml', 'home_team', 'visit_team']
        for ii in games:
            if not Game.objects.filter(home_team=ii['home_team'], visit_team=ii['visit_team'], data_source=data_source).exists():
                defaults = { key: str(ii[key]).replace(',', '') for key in fields }
                defaults['date'] = datetime.datetime.strptime(ii['date'][5:], '%I:%M %p')
                # date is not used
                defaults['date'] = datetime.datetime.combine(datetime.date.today(), defaults['date'].time())
                defaults['ou'] = float(ii['ou']) if ii['ou'] else 0
                defaults['data_source'] = data_source
                defaults['home_score'] = html2text.html2text(ii['home_score']).strip()
                defaults['visit_score'] = html2text.html2text(ii['visit_score']).strip()
                Game.objects.create(**defaults)


if __name__ == "__main__":
    for id, ds in enumerate(DATA_SOURCE, 1):
        get_games(ds[0], id)
