def test_get_activities_returns_expected_shape(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, dict)
    assert len(data) > 0

    for activity_name, details in data.items():
        assert isinstance(activity_name, str)
        assert isinstance(details, dict)
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
