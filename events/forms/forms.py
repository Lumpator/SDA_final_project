from django.forms import ModelForm

from events_api.models import Event


class EventCreateForm(ModelForm):

    class Meta:
        model = Event
        fields = ["title", "description", "event_start", "event_end", "city"]

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'