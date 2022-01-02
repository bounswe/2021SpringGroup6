#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests

def normalize_name(sport_name):
    sport_name = sport_name.lower()
    name_list = sport_name.split(' ')
    return '_'.join(name_list)

def sport_records():
    from sports_platform_api.models.sport_models import Sport
    uri = 'https://www.thesportsdb.com/api/v1/json/2/all_sports.php'
    try:
        sports = requests.get(uri).json()
        for sport in sports['sports']:
            try:
                sport_name = normalize_name(sport['strSport'])
                Sport.objects.create(name=sport_name)
            except: # Already exists
                pass
    except:
        pass # error from external library so skip

    Sport.objects.create(name="ultimate_frisbee")

def add_badges():
    from sports_platform_api.data import badges
    from sports_platform_api.models import Badge

    for badge in badges:
        try:
            if 'wikidata' in badge:
                if 'sport' in badge:
                    Badge.objects.create(name=badge['name'], wikidata=badge['wikidata'], sport_id=badge['sport'])
                else:
                    Badge.objects.create(name=badge['name'], wikidata=badge['wikidata'])
            else:
                if 'sport' in badge:
                    Badge.objects.create(name=badge['name'], sport_id=badge['sport'])
                else:
                    Badge.objects.create(name=badge['name'])
        except: # Already exists
            pass


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_platform.settings')
    try:

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    sport_records()
    add_badges()


if __name__ == '__main__':
    main()
