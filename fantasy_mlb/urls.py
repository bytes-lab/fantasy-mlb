from django.conf.urls import url
from django.contrib import admin

from general.views import *

admin.site.site_header = "Green Light MLB"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lineup_optimizer, name="lineup_optimizer"),
    url(r'^lineup-optimizer$', lineup_optimizer, name="lineup_optimizer"),
    url(r'^lineup-builder$', lineup_builder, name="lineup_builder"),
    url(r'^build-lineup$', build_lineup, name="build_lineup"),
    url(r'^gen-lineups', gen_lineups, name="gen_lineups"),
    url(r'^check-mlineups', check_mlineups, name="check_mlineups"),
    url(r'^export_lineups', export_lineups, name="export_lineups"),
    url(r'^export-mlineup', export_manual_lineup, name="export_manual_lineup"),
    url(r'^get-players', get_players, name="get_players"),
    url(r'^get-games', get_games, name="get_games"),
    url(r'^get-slates', get_slates, name="get_slates"),
    url(r'^upload-data$', upload_data),
    url(r'^trigger-scraper', trigger_scraper, name="trigger_scraper"),
    url(r'^update-point', update_point, name="update_point"),
    url(r'^update-field', update_field, name="update_field"),
    url(r'^get-team-stack-dlg/(?P<ds>.+)', get_team_stack_dlg, name="get_team_stack_dlg"),
    url(r'^slates/(?P<slate_id>\d+)', load_slate, name="load_slate"),
]
