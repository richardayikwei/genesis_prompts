from datetime import datetime
import yaml

from .prompt_loader import load_prompts


SECTION_PREFIX = {
    "idea": "idea",
    "feature": "feat",
    "refactor": "ref"
}


def _generate_id(entries, prefix):
    """Generate next ID based on existing entries."""
    if not entries:
        return f"{prefix}-001"

    last_id = entries[-1]["id"]
    number = int(last_id.split("-")[1]) + 1
    return f"{prefix}-{number:03d}"


def append_prompt(section, agent, prompt_text):
    """
    Append a new prompt to the .prompts file.
    """

    if section not in SECTION_PREFIX:
        raise ValueError(f"Invalid section '{section}'")

    # Load current data + path
    data, path = load_prompts()

    # Ensure section + agent exist
    data.setdefault(section, {})
    data[section].setdefault(agent, [])

    entries = data[section][agent]

    # Generate ID
    prefix = SECTION_PREFIX[section]
    new_id = _generate_id(entries, prefix)

    # Create entry
    entry = {
        "id": new_id,
        "prompt": prompt_text,
        "created_at": datetime.now().isoformat()
    }

    # Append
    entries.append(entry)

    # Write back to file
    with open(path, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False)

    return entry