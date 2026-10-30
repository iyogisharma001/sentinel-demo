class InvalidToken(Exception):
    pass


def get_subject(payload):
    return payload["sub"].strip()
