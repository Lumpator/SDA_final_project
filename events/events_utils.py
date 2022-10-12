from datetime import datetime, timedelta
from typing import List

from events_api.models import Event


def check_and_save_session_filters(request):
    if request.POST.get("datestart"):
        request.session["datestart"] = request.POST.get("datestart")
    if request.POST.get("dateend"):
        request.session["dateend"] = request.POST.get("dateend")
    if request.POST.getlist("locations"):
        request.session["locations"] = request.POST.getlist("locations")
    request.session["favourites_checkbox"] = request.POST.get("favourites_checkbox", False)
    request.session["joined_checkbox"] = request.POST.get("joined_checkbox", False)

    return request


def add_day_for_filter(dateend):
    if isinstance(dateend, str):
        return datetime.strptime(dateend, "%Y-%m-%d") + timedelta(days=1)
    return dateend


def get_all_cities_from_events():
    cities = set()
    for event in Event.objects.all():
        cities.add(event.city)
    return sorted(list(cities))


def execute_filtered_query(request, filters: List, default: List):
    events = Event.objects.filter(event_start__gte=request.session.get("datestart", default[0])).filter(
        event_start__lte=add_day_for_filter(request.session.get("dateend", default[1])))
    if "All locations" not in filters[2]:
        events = events.filter(city__in=filters[2])
    if request.session.get("favourites_checkbox"):
        events = events.filter(favourites__username__exact=request.user.username)
    if request.session.get("joined_checkbox"):
        events = events.filter(participants__username__exact=request.user.username)
    return events


def get_filters_from_session(request):
    filters = [request.session.get("datestart"), request.session.get("dateend"),
               request.session.get("locations", "All locations"), request.session.get("favourites_checkbox"), request.session.get("joined_checkbox")]
    return filters