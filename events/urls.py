from django.urls import path

import events.views

urlpatterns = [
    path('', events.views.home, name="home"),
    # filtering endpoints
    path("event/<str:id>", events.views.event_detail, name="event_detail"),
    path("event/<str:id>/addfav", events.views.add_event_to_favourites, name="add_favourites"),
    path("event/<str:id>/rmfav", events.views.remove_event_from_favourites, name="rm_favourites"),
    path("event/<str:id>/join", events.views.join_event, name="join_event"),
    path("event/<str:id>/leave", events.views.leave_event, name="leave_event"),
    path("event/<str:id>/create_message", events.views.create_message, name="create_message"),
    path("create/", events.views.create_event, name="create_event"),
    path("search/", events.views.search, name="search"),
    path("my-events", events.views.my_events, name="my_events"),
    path("event/<str:id>/delete", events.views.delete_event, name="delete_event"),
    path("event/<str:id>/edit", events.views.edit_event, name="edit_event"),
    path("event/<str:id>/update_photo", events.views.update_photo, name="update_photo"),


]
