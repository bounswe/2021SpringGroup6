def _event_full(notification):
    return {
            "description": f"The event with name {notification.event_id.name} is full now.",
            "notification_id": notification.id,
            "event_id": notification.event_id.event_id,
            "date": notification.date,
            "type": notification.type
    }

def _event_accept(notification):
    return {
            "description": f"You are accpeted for the event with name {notification.event_id.name}",
            "notification_id": notification.id,
            "event_id": notification.event_id.event_id,
            "date": notification.date,
            "type": notification.type
    }

def _event_reject(notification):
    return {
            "description": f"You are rejected for the event with name {notification.event_id.name}",
            "notification_id": notification.id,
            "event_id": notification.event_id.event_id,
            "date": notification.date,
            "type": notification.type
    }

def _event_cancel(notification):
    return {
            "description": f"The event with name {notification.event_id.name} that you will participate is cancelled",
            "notification_id": notification.id,
            "event_id": notification.event_id.event_id,
            "date": notification.date,
            "type": notification.type
    }

def _event_update(notification):
    return {
            "description": f"The event with name {notification.event_id.name} that you will participate is updated",
            "notification_id": notification.id,
            "event_id": notification.event_id.event_id,
            "date": notification.date,
            "type": notification.type
    }

def _few_spot(notification):
    spot = notification.type.split(' ')[0]
    return {
            "description": f"only {spot} spots left for the event with name {notification.event_id.name}",
            "notification_id": notification.id,
            "event_id": notification.event_id.event_id,
            "date": notification.date,
            "type": "Few Spot Left for an Event"
    }

def prepare_notifications(notifications):
    functions = {'Event Full':_event_full, 'Event Acceptance': _event_accept, 'Event Rejection': _event_reject,
                'Event Cancellation': _event_cancel, "Event Update": _event_update}
    response = {"@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Notifications",
            "type": "Collection",
            "total_items": len(notifications)} 
    items = []
    for notification in notifications:
        if notification.type not in functions:
            items.append(_few_spot(notification))
        else:
            items.append(functions[notification.type](notification))
    response['Items'] = items
    return response
