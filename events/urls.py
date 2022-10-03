from django.urls import path

import events.views

urlpatterns = [
    path('', events.views.home),
]