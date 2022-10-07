from datetime import datetime, timedelta
from time import strptime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from events.events_utils import check_and_save_session_filters, add_day_for_filter, get_all_cities_from_events, \
    execute_filtered_query, get_filters_from_session
from events_api.models import Event


# Create your views here.

def home(request):
    # session handling - create new for annonymous user
    if not request.session or not request.session.session_key:
        request.session.save()
    check_and_save_session_filters(
        request)  # save filtered settings (if any) into session. Also rewrite old ones if new filter was set.
    filters = get_filters_from_session(request)
    default = [datetime.today(), datetime.today() + timedelta(weeks=4)]  # for template purposes

    events = execute_filtered_query(request, filters, default)

    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "event_listing_with_pagination_block.html",
                  {"page_obj": page_obj, "filters": filters, "default": default,
                   "cities": get_all_cities_from_events()})
