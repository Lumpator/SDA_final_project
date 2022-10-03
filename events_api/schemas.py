from ninja import ModelSchema
from events_api.models import Event


class EventOut(ModelSchema):
    class Config:
        model = Event
        model_fields = ["title", "description", "event_start", "event_end", "city"]

class EventIn(ModelSchema):
    class Config:
        model = Event
        model_fields = ["title", "description", "event_start", "event_end", "city"]