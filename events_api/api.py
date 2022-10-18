from time import strptime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from ninja import Router, Form, File, UploadedFile

from accounts.models import CustomUser
from events_api.models import Event
from events_api.schemas import EventOut, EventIn

router = Router()


@router.get("/{int:event_id}", response=EventOut)
def one_event(request, event_id):
    return get_object_or_404(Event, pk=event_id)


@router.get("/all", response=list[EventOut])
def all_events(request):
    return get_list_or_404(Event)


@router.post("/create")
def create_event(request, event: EventIn = Form(...), file: UploadedFile = None):
    new_event = Event(**event.dict())
    new_event.host = CustomUser.objects.get(username="lumpator")
    new_event.photo = file
    file_storage = FileSystemStorage()
    file_url = file_storage.url(file)
    new_event.save()
    new_event.photo = file_url
    new_event.save()
    return JsonResponse({"id": new_event.id}, status=201)



