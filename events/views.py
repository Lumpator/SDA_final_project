import json
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.models import CustomUser
from events.events_utils import check_and_save_session_filters, get_all_cities_from_events, \
    execute_filtered_query, get_filters_from_session
from events.forms.forms import EventCreateForm
from events.models import Message
from events_api.models import Event


# Create your views here.

def home(request, *args, **kwargs):
    # session handling - create new for annonymous user
    if not request.session or not request.session.session_key:
        request.session.save()
    if request.method == "POST":
        print(request.POST.get("datestart"))
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
    messages = Message.objects.filter(event=event)
    return render(request, "event_detail.html", {"event": event, "messages": messages})


@login_required
def add_event_to_favourites(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.favourites.add(user)
        event.save()
        return HttpResponse("OK")


@login_required
def remove_event_from_favourites(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.favourites.remove(user)
        event.save()
        return HttpResponse("OK")


@login_required
def join_event(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.participants.add(user)
        event.save()
        return HttpResponse("OK")


@login_required
def leave_event(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=request.user.id)
        event = Event.objects.get(id=id)
        event.participants.remove(user)
        event.save()
        return HttpResponse("OK")


@login_required
def create_event(request):
    form = EventCreateForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form_photo = request.FILES["photo"]
            file_storage = FileSystemStorage()
            file = file_storage.save(form_photo.name, form_photo)
            file_url = file_storage.url(file)
            event = Event.objects.create(
                host=request.user,
                title=request.POST.get("title"),
                description=request.POST.get("description"),
                event_start=request.POST.get("event_start"),
                event_end=request.POST.get("event_end"),
                city=request.POST.get("city"),
                photo=file_url

            )
            return redirect("event_detail", id=event.id)

    return render(request, "create_event.html", {"form": EventCreateForm})


@login_required
def create_message(request, id):
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            event=Event.objects.get(pk=request.POST.get("event_id")),
            body=request.POST.get("body")
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def search(request):
    if request.method == "POST":
        if request.POST.get("event_search"):
            search_query = request.POST.get("event_search").strip()
            if len(search_query) > 0:
                events = Event.objects.filter(title__icontains=search_query).filter(event_start__gt=request.POST.get("startdate"))
                descr_results = Event.objects.filter(description__icontains=search_query)
            else:
                return redirect(request.META.get('HTTP_REFERER'))

            return render(request, "search_results.html",
                          {"events": events,
                           "search_query": search_query})
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/')
