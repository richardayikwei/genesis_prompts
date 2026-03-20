from pathlib import Path
import yaml
import tomllib  # Python 3.11+


DEFAULT_CONFIG = {
    "file": ".prompts",
    "auto_create": True
}


def find_project_root():
    current = Path.cwd()

    for parent in [current] + list(current.parents):
        if (parent / "pyproject.toml").exists():
            return parent

    return current


def load_config(root: Path):
    config_path = root / "pyproject.toml"

    if not config_path.exists():
        return DEFAULT_CONFIG

    with open(config_path, "rb") as f:
        data = tomllib.load(f)

    return data.get("tool", {}).get("genesisprompts", DEFAULT_CONFIG)


def load_prompts():
    root = find_project_root()
    config = load_config(root)

    file_path = root / config.get("file", ".prompts")

    if not file_path.exists() and config.get("auto_create", True):
        print("[genesis] Creating .prompts file...")
        with open(file_path, "w") as f:
            yaml.safe_dump({
                "version": 1,
                "idea": {},
                "feature": {},
                "refactor": {}
            }, f, sort_keys=False)

    with open(file_path, "r") as f:
        data = yaml.safe_load(f) or {}

    return data, file_path