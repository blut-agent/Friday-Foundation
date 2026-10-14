"""Evidence-bound schema tests for the sales-call-review command: missing dates and owners get explicit paths."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = REPO_ROOT / "commands"


def test_sales_call_review_missing_evidence_has_schema_paths():
    """No schema shape forces fabrication: missing dates and owners get explicit 'not stated' paths."""
    text = (COMMANDS_DIR / "sales-call-review.md").read_text(encoding="utf-8")

    assert "\"date not stated\"" in text, (
        "the per-call entry heading must allow a missing date rather than forcing one"
    )
    assert "owner: not stated" in text, (
        "next actions must allow a missing owner rather than forcing an assignment"
    )
    assert "rather than guessing who owns it" in text, (
        "the owner rule must say the assignment is not a guess"
    )
