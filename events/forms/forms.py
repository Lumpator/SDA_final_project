from django.core.exceptions import ValidationError
from django.forms import ModelForm

from events_api.models import Event




class EventCreateForm(ModelForm):

    class Meta:
        model = Event
        fields = ["title", "description", "city", "photo"]



    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['photo'].label = "Add Event photo (for best result use 16:9 scale)"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

