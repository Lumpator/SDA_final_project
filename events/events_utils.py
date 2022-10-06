from datetime import datetime, timedelta


def check_and_save_session_filters(request):
    if request.GET.get("datestart"):
        request.session["datestart"] = request.GET.get("datestart")
    if request.GET.get("dateend"):
        request.session["dateend"] = request.GET.get("dateend")
    return request

def add_day_for_filter(dateend):
    if isinstance(dateend, str):
        return datetime.strptime(dateend, "%Y-%m-%d") + timedelta(days=1)
    return dateend