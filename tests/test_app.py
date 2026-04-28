def test_get_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    body = response.json()
    assert "Chess Club" in body
    assert body["Programming Class"]["max_participants"] == 20


def test_signup_for_activity(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "test.student@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Signed up test.student@mergington.edu for Chess Club"
    }


def test_signup_for_missing_activity(client):
    response = client.post(
        "/activities/Unknown/signup",
        params={"email": "test.student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_student(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_unregister_from_activity(client):
    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }


def test_unregister_from_missing_activity(client):
    response = client.delete(
        "/activities/Unknown/unregister",
        params={"email": "test.student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_student_not_signed_up(client):
    response = client.delete(
        "/activities/Basketball Team/unregister",
        params={"email": "samuel@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student not signed up for this activity"
