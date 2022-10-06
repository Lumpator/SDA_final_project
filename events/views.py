from datetime import datetime, timedelta
from time import strptime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from events.events_utils import check_and_save_session_filters, add_day_for_filter
from events_api.models import Event


# Create your views here.

def home(request):
    # session handling - create new for annonymous user
    if not request.session or not request.session.session_key:
        request.session.save()
    check_and_save_session_filters(
        request)  # save filter data (if any) into session. Also rewrite old ones if new filter was set.

    filters = [request.session.get("datestart"), request.session.get("dateend")]  # for template purposes
    default = [datetime.today(), datetime.today() + timedelta(weeks=4)]  # for template purposes

    events = Event.objects.filter(event_start__gte=request.session.get("datestart", default[0])).filter(
        event_start__lte=add_day_for_filter(request.session.get("dateend", default[1])))
    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "event_listing_with_pagination_block.html",
                  {"page_obj": page_obj, "filters": filters, "default": default})


