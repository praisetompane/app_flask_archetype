from app_flask_archetype.api.validator import validate


def test_validation():
    assert validate(None) is True
