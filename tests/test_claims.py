from src.auth.claims import get_subject


def test_get_subject_basic():
    assert get_subject({"sub": " alice "}) == "alice"
