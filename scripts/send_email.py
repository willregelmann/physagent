#!/usr/bin/env python3
"""Send a plain-text email via SMTP (STARTTLS). Stdlib only.

Used by the breakthrough-alert and digest workflows (instrumentation tier;
see the EXPERIMENT.md log entry of 2026-06-10). Degrades gracefully: if SMTP
credentials are not configured, prints a notice and exits 0 so a missing
secret can never fail a workflow — delivery falls back to the dashboard
issue / workflow log.

Environment:
  SMTP_USERNAME, SMTP_PASSWORD  -- credentials (repo secrets); for Gmail use
                                   an app password
  MAIL_TO                       -- recipient (repo variable ALERT_EMAIL)
  MAIL_SUBJECT                  -- subject line
  SMTP_HOST                     -- optional, default smtp.gmail.com
  SMTP_PORT                     -- optional, default 587

The message body is read from stdin.
"""
import os
import smtplib
import sys
from email.message import EmailMessage


def main() -> int:
    user = os.environ.get("SMTP_USERNAME", "")
    password = os.environ.get("SMTP_PASSWORD", "")
    to = os.environ.get("MAIL_TO", "")
    if not (user and password and to):
        print(
            "::notice::SMTP_USERNAME / SMTP_PASSWORD / MAIL_TO not configured "
            "-- email skipped; content is on the dashboard issue / workflow log."
        )
        return 0

    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = to
    msg["Subject"] = os.environ.get("MAIL_SUBJECT", "self-consistency notification")
    msg.set_content(sys.stdin.read())

    host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("SMTP_PORT", "587"))
    with smtplib.SMTP(host, port, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)
    print(f"Sent {msg['Subject']!r} to {to}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
