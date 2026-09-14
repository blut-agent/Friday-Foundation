"""/one-on-one-prep: a brief beats an agenda only if it is honest about its gaps.

The command's claim is that it carries relationship context, the topics still
open, the feedback owed, the outcome wanted, and the commitments to leave with,
and that it never invents personal context to fill a hole. These tests hold the
command to both halves of that claim, plus the issue's no-contact guarantee.
"""
from pathlib import Path

from tests.test_commands import parse_frontmatter

REPO_ROOT = Path(__file__).parent.parent
COMMAND_PATH = REPO_ROOT / "commands" / "one-on-one-prep.md"


def get_one_on_one_prep_command() -> str:
    return COMMAND_PATH.read_text(encoding="utf-8")


def test_frontmatter_declares_the_issue_contract():
    text = get_one_on_one_prep_command()
    fm, body = parse_frontmatter(text)

    assert fm["name"] == "one-on-one-prep"
    assert "friday/voice.md" in fm["description"]
    assert "friday/one-on-ones/<person>.md" in fm["description"]
    assert "# /one-on-one-prep" in body


def test_captures_every_input_the_issue_names():
    """Drop any one of these and the brief stops being about the relationship."""
    text = get_one_on_one_prep_command()
    for field in (
        "**The person.**",
        "**Relationship context.**",
        "**Open topics.**",
        "**Feedback.**",
        "**Desired outcome.**",
    ):
        assert field in text, f"input missing from the command: {field}"


def test_brief_sections_cover_context_topics_feedback_outcome_and_questions():
    text = get_one_on_one_prep_command()
    for section in (
        "### The person and the relationship",
        "### What is open from last time",
        "### Feedback to give",
        "### The outcome you want",
        "### Questions worth asking",
        "### Commitments to leave with",
    ):
        assert section in text, f"brief section missing: {section}"


def test_separates_stated_from_assumed():
    text = get_one_on_one_prep_command()
    assert "**Stated:**" in text
    assert "**Assumed:**" in text
    assert "Do not fabricate context, history, sentiment, or quotes." in text


def test_missing_input_is_named_not_invented():
    """The failure mode that makes a brief worse than no brief at all."""
    text = get_one_on_one_prep_command()
    assert "`not given` rather than inventing a plausible answer" in text
    assert "It does not invent personal context." in text


def test_refuses_to_contact_or_schedule():
    text = get_one_on_one_prep_command()
    assert "does not message the person, schedule the meeting" in text
    assert "does not read your calendar" in text


def test_writes_one_file_per_person_and_never_overwrites():
    text = get_one_on_one_prep_command()
    assert "Create the `friday/` folder if it does not exist" in text
    assert "Create the `friday/one-on-ones/` folder if it does not exist" in text
    assert "append the new brief under a `---` separator rather than overwriting" in text
    assert "One-on-one brief saved to `friday/one-on-ones/<person>.md`" in text


def test_no_em_dashes():
    text = get_one_on_one_prep_command()
    assert "\u2014" not in text and "\u2013" not in text


def test_file_ends_with_a_newline():
    assert get_one_on_one_prep_command().endswith("\n")
