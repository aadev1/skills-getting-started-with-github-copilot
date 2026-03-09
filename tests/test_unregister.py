def test_unregister_success_removes_participant(client):
    activities = client.get("/activities").json()
    activity_name = "Chess Club"
    participant_email = activities[activity_name]["participants"][0]

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": participant_email},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {participant_email} from {activity_name}"
    }

    updated_activities = client.get("/activities").json()
    assert participant_email not in updated_activities[activity_name]["participants"]


def test_unregister_participant_not_found(client):
    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": "missing.student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found in this activity"}


def test_unregister_activity_not_found(client):
    response = client.delete(
        "/activities/Unknown Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
