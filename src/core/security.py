import re

RE_EMAIL = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
RE_PHONE = re.compile(r"\b(?:\+\d{1,3}[- ]?)?\d{3}[- ]?\d{3}[- ]?\d{4}\b")
RE_TOKEN = re.compile(r"sk-[A-Za-z0-9]{16,}")


def redact(text: str) -> str:
    """Mask common PII/secrets prior to logging."""
    if not text:
        return text
    masked = RE_EMAIL.sub("[EMAIL]", text)
    masked = RE_PHONE.sub("[PHONE]", masked)
    masked = RE_TOKEN.sub("[TOKEN]", masked)
    return masked

