class InvalidToken(Exception):
    pass


def get_subject(payload):
    subject = payload.get("sub")
    if not subject or not subject.strip():
        raise InvalidToken("subject is required")
    return subject.strip()