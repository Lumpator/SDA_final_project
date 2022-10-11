from datetime import datetime, timedelta
from time import strptime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import CustomUser
from events.events_utils import check_and_save_session_filters, add_day_for_filter, get_all_cities_from_events, \
    execute_filtered_query, get_filters_from_session
from events_api.models import Event


# Create your views here.

def home(request):
    # session handling - create new for annonymous user
    if not request.session or not request.session.session_key:
        request.session.save()
    if request.method == "POST":
        check_and_save_session_filters(
            request)  # save filtered settings (if any) into session. Also rewrite old ones if new filter was set.
    filters = get_filters_from_session(request)
    default = [datetime.today(), datetime.today() + timedelta(weeks=4)]  # for template purposes

    events = execute_filtered_query(request, filters, default)

    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html",
                  {"page_obj": page_obj, "filters": filters, "default": default,
                   "cities": get_all_cities_from_events()})


@login_required
def event_detail(request, id):
    if request.method == "POST":
        return HttpResponse("success")
    event = Event.objects.get(pk=id)
    return render(request, "event_detail.html", {"event": event})


def add_event_to_favourites(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.favourites.add(user)
        event.save()
        return HttpResponse("OK")


def remove_event_from_favourites(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.favourites.remove(user)
        event.save()
        return HttpResponse("OK")

def join_event(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.participants.add(user)
        event.save()
        return HttpResponse("OK")

def leave_event(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.participants.remove(user)
        event.save()
        return HttpResponse("OK")

