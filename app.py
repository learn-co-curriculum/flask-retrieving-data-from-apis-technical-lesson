from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data store — persists in memory while the server is running
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Tracks the next available ID (auto-increment simulation)
next_id = 3


@app.route("/events", methods=["POST"])
def create_event():
    """POST /events — Create a new event from JSON input."""
    global next_id

    data = request.get_json()

    # Validate that a body was sent and that it contains a valid title
    if not data or "title" not in data:
        return jsonify({"error": "Event title is required"}), 400

    title = data["title"]
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Event title is required"}), 400

    title = title.strip()

    # Create the new event and append it to the in-memory list
    new_event = Event(id=next_id, title=title)
    events.append(new_event)
    next_id += 1

    # 201 Created — standard response for a successful resource creation
    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    """PATCH /events/<id> — Update the title of an existing event."""
    data = request.get_json()

    # Validate request body before touching any data
    if not data or "title" not in data:
        return jsonify({"error": "Event title is required"}), 400

    title = data["title"]
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Event title is required"}), 400

    title = title.strip()

    # Search for the event by ID
    for event in events:
        if event.id == id:
            event.title = title
            return jsonify(event.to_dict()), 200

    # 404 if no event matched the given ID
    return jsonify({"error": "Event not found"}), 404


@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    """DELETE /events/<id> — Remove an event from the list."""
    for event in events:
        if event.id == id:
            events.remove(event)
            # 200 with a confirmation message (204 would return no body)
            return jsonify({"message": "Event deleted successfully"}), 200

    # 404 if no event matched the given ID
    return jsonify({"error": "Event not found"}), 404


@app.route("/events", methods=["GET"])
def list_events():
    """GET /events — List all events (useful for verifying state during testing)."""
    return jsonify([e.to_dict() for e in events]), 200


if __name__ == "__main__":
    app.run(debug=True)