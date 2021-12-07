def _block(activity):
    return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": f"{activity.actor.identifier} blocked {activity.object.identifier}",
            "id": activity.id,
            "type": "Block",
            "actor": {
                "type": "https://schema.org/Person", 
                "@id": activity.actor.user_id,
                "identifier": activity.actor.identifier
            },
            "object": {
                "type": "https://schema.org/Person", 
                "@id": activity.object.user_id,
                "identifier": activity.object.identifier
            },
    }

def _follow(activity):
    return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": f"{activity.actor.identifier} followed {activity.object.identifier}",
            "id": activity.id,
            "type": "Follow",
            "actor": {
                "type": "https://schema.org/Person", 
                "@id": activity.actor.user_id,
                "identifier": activity.actor.identifier
            },
            "object": {
                "type": "https://schema.org/Person", 
                "@id": activity.object.user_id,
                "identifier": activity.object.identifier
            }
    }

def _create_event(activity):
    return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": f"{activity.actor.identifier} created {activity.target.name}",
            "id": activity.id,
            "type": "Create",
            "actor": {
                "type": "https://schema.org/Person", 
                "@id": activity.actor.user_id,
                "identifier": activity.actor.identifier
            },
            "object": {
                "type": "https://schema.org/Event", 
                "@id": activity.target.event_id,
                "name": activity.target.name
            },
    }

def _accept_event(activity):
    return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": f"{activity.actor.identifier} accepted {activity.object.identifier} for {activity.target.name}",
            "id": activity.id,
            "type": "Accept",
            "actor": {
                "type": "https://schema.org/Person", 
                "@id": activity.actor.user_id,
                "identifier": activity.actor.identifier
            },
            "object": {
                "type": "https://schema.org/Person", 
                "@id": activity.object.user_id,
                "identifier": activity.object.identifier
            },
            "target": {
                "type": "https://schema.org/Event", 
                "@id": activity.target.event_id,
                "name": activity.target.name
            },
    }

def _spectator(activity):
    return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": f"{activity.actor.identifier} joins to {activity.target.name} as a spectator",
            "id": activity.id,
            "type": "Activity",
            "actor": {
                "type": "https://schema.org/Person", 
                "@id": activity.actor.user_id,
                "identifier": activity.actor.identifier
            },
            "target": {
                "type": "https://schema.org/Event", 
                "@id": activity.target.event_id,
                "name": activity.target.name
            },
    }


def create_activity_response(activities):
    functions = {'Block':_block, 'Follow': _follow, 'Create': _create_event,
                'Accept': _accept_event, "Activity": _spectator}
    response = {"@context": "https://www.w3.org/ns/activitystreams",
                "summary": "Activity stream",
                "type": "OrderedCollection",
                "total_items": len(activities)} 
    items = []
    for activity in activities:
        items.append(functions[activity.type](activity))

    response['orderedItems'] = items
    return response
