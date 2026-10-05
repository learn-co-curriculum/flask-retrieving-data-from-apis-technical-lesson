import pytest

import app as app_module


@pytest.fixture(autouse=True)
def reset_events():
    original_events = list(app_module.events)
    app_module.events.clear()
    app_module.events.extend([
        app_module.Event(1, "Tech Meetup"),
        app_module.Event(2, "Python Workshop"),
    ])
    yield
    app_module.events.clear()
    app_module.events.extend(original_events)


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_create_event_returns_201_and_new_event(client):
    response = client.post(
        "/events",
        json={"title": "AI Conference"},
    )

    assert response.status_code == 201
    assert response.get_json() == {"id": 3, "title": "AI Conference"}
    assert len(app_module.events) == 3


def test_create_event_requires_title(client):
    response = client.post("/events", json={"description": "no title here"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Event title is required"}


def test_update_event_changes_title(client):
    response = client.patch(
        "/events/1",
        json={"title": "Updated Meetup"},
    )

    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "title": "Updated Meetup"}
    assert app_module.events[0].title == "Updated Meetup"


def test_delete_event_removes_event(client):
    response = client.delete("/events/2")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Event deleted successfully"}
    assert [event.id for event in app_module.events] == [1]


def test_delete_event_missing_event_returns_404(client):
    response = client.delete("/events/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Event not found"}
