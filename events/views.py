from django.shortcuts import render, get_object_or_404
from .models import Event

# List of events
def event_list(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'events/event_list.html', {'events': events})

# Event detail view
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch a specific event by ID
    return render(request, 'events/event_detail.html', {'event': event})

# Event creation form (view)
def create_event(request):
    if request.method == 'POST':
        # Add logic to handle form submission
        pass
    return render(request, 'events/event_form.html')  # Render the event creation form
