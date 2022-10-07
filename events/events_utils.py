from datetime import datetime, timedelta
from typing import List

from events_api.models import Event


def check_and_save_session_filters(request):
    if request.GET.get("datestart"):
        request.session["datestart"] = request.GET.get("datestart")
    if request.GET.get("dateend"):
        request.session["dateend"] = request.GET.get("dateend")
    if request.GET.getlist("locations"):
        request.session["locations"] = request.GET.getlist("locations")
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
    return events


def get_filters_from_session(request):
    filters = [request.session.get("datestart"), request.session.get("dateend"),
               request.session.get("locations", "All locations")]
    return filters