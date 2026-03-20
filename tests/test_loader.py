import pytest
from pathlib import Path
from genesisprompts.prompt_loader import load_prompts, find_project_root, load_config


def test_creates_prompts_file_if_missing(tmp_path, monkeypatch):
    # simulate project root
    project_root = tmp_path
    (project_root / "pyproject.toml").write_text("")

    # change working directory
    monkeypatch.chdir(project_root)

    data, path = load_prompts()

    assert path.exists()
    assert path.name == ".prompts"
    assert "idea" in data
    assert "feature" in data
    assert "refactor" in data


def test_find_project_root(tmp_path, monkeypatch):
    root = tmp_path / "project"
    root.mkdir()

    subdir = root / "src" / "app"
    subdir.mkdir(parents=True)

    # create pyproject.toml at root
    (root / "pyproject.toml").write_text("")

    # simulate running inside subdir
    monkeypatch.chdir(subdir)

    detected_root = find_project_root()

    assert detected_root == root

def test_find_project_root_fallback(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    root = find_project_root()

    assert root == tmp_path


def test_load_config_defaults(tmp_path):
    config = load_config(tmp_path)

    assert config["file"] == ".prompts"
    assert config["auto_create"] is True

def test_load_config_reads_pyproject(tmp_path):
    (tmp_path / "pyproject.toml").write_text("""
[tool.genesisprompts]
file = "custom.prompts"
auto_create = false
""")

    config = load_config(tmp_path)

    assert config["file"] == "custom.prompts"
    assert config["auto_create"] is False