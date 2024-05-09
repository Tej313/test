# conftest.py
import pytest

@pytest.fixture
def user_profiles():
    """Provide sample user data for tests."""
    return [
        {'name': 'Alice', 'age': 28, 'active': True},
        {'name': 'Bob', 'age': 34, 'active': False},
        {'name': 'Charlie', 'age': 22, 'active': True}
    ]
# test_profiles.py
def test_active_users(user_profiles):
    """Test to ensure there are active users in the user profiles."""
    active_users = [user for user in user_profiles if user['active']]
    assert len(active_users) > 0  # Check that there is at least one active user
