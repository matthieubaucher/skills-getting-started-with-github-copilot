import copy

from fastapi.testclient import TestClient
import pytest

from src.app import app, activities


@pytest.fixture
def client():
    original_activities = copy.deepcopy(activities)
    with TestClient(app) as test_client:
        yield test_client
    activities.clear()
    activities.update(original_activities)
