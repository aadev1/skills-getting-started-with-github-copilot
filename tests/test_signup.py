def test_signup_success_adds_participant(client):
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}

    activities = client.get("/activities").json()
    assert email in activities[activity_name]["participants"]


def test_signup_duplicate_student_fails(client):
    email = "duplicate.student@mergington.edu"

    first_response = client.post("/activities/Chess Club/signup", params={"email": email})
    second_response = client.post("/activities/Soccer Club/signup", params={"email": email})

    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert second_response.json() == {"detail": "Student already signed up for an activity"}


def test_signup_activity_not_found(client):
    response = client.post("/activities/Unknown Club/signup", params={"email": "test@mergington.edu"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
