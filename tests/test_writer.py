import pytest
from pathlib import Path
import yaml

from genesisprompts.prompt_writer import append_prompt


# Helper to simulate project root
def setup_project(tmp_path, monkeypatch, config_content=None):
    # create pyproject.toml
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(config_content or "")

    # move into that directory
    monkeypatch.chdir(tmp_path)

    return tmp_path


# -------------------------
# TEST 1: file creation
# -------------------------
def test_writer_creates_prompts_file(tmp_path, monkeypatch):
    setup_project(tmp_path, monkeypatch)

    entry = append_prompt("feature", "chat", "Test prompt")

    prompts_file = tmp_path / ".prompts"

    assert prompts_file.exists()
    assert entry["id"] == "feat-001"


# -------------------------
# TEST 2: first entry
# -------------------------
def test_append_first_entry(tmp_path, monkeypatch):
    setup_project(tmp_path, monkeypatch)

    entry = append_prompt("idea", "chat", "Initial idea")

    assert entry["id"] == "idea-001"
    assert "created_at" in entry


# -------------------------
# TEST 3: ID increments
# -------------------------
def test_append_increments_id(tmp_path, monkeypatch):
    setup_project(tmp_path, monkeypatch)

    append_prompt("feature", "chat", "First")
    entry = append_prompt("feature", "chat", "Second")

    assert entry["id"] == "feat-002"


# -------------------------
# TEST 4: different agents
# -------------------------
def test_separate_agents(tmp_path, monkeypatch):
    setup_project(tmp_path, monkeypatch)

    append_prompt("feature", "chat", "Chat prompt")
    append_prompt("feature", "copilot", "Copilot prompt")

    with open(tmp_path / ".prompts") as f:
        data = yaml.safe_load(f)

    assert "chat" in data["feature"]
    assert "copilot" in data["feature"]
    assert len(data["feature"]["chat"]) == 1
    assert len(data["feature"]["copilot"]) == 1


# -------------------------
# TEST 5: different sections
# -------------------------
def test_separate_sections(tmp_path, monkeypatch):
    setup_project(tmp_path, monkeypatch)

    append_prompt("idea", "chat", "Idea prompt")
    append_prompt("feature", "chat", "Feature prompt")

    with open(tmp_path / ".prompts") as f:
        data = yaml.safe_load(f)

    assert "idea" in data
    assert "feature" in data
    assert len(data["idea"]["chat"]) == 1
    assert len(data["feature"]["chat"]) == 1


# -------------------------
# TEST 6: invalid section
# -------------------------
def test_invalid_section_raises(tmp_path, monkeypatch):
    setup_project(tmp_path, monkeypatch)

    with pytest.raises(ValueError):
        append_prompt("invalid", "chat", "Bad prompt")