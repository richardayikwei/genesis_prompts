# genesisprompts/genesis.py

from .prompt_loader import load_prompts
from .prompt_writer import append_prompt


VALID_SECTIONS = ["idea", "feature", "refactor"]


class Genesis:
    def __init__(self):
        self.data, self.path = load_prompts()

    # -------------------------
    # Core action: add prompt
    # -------------------------
    def add_prompt(self, section: str, agent: str, prompt: str):
        self._validate_section(section)
        self._validate_agent(agent)
        self._validate_prompt(prompt)

        entry = append_prompt(section, agent, prompt)

        return entry

    # -------------------------
    # Helpers
    # -------------------------
    def _validate_section(self, section):
        if section not in VALID_SECTIONS:
            raise ValueError(
                f"Invalid section '{section}'. Choose from {VALID_SECTIONS}"
            )

    def _validate_agent(self, agent):
        if not agent or not isinstance(agent, str):
            raise ValueError("Agent must be a non-empty string")

    def _validate_prompt(self, prompt):
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

    # -------------------------
    # Read operations (useful later)
    # -------------------------
    def get_all_prompts(self):
        return self.data

    def list_agents(self):
        agents = set()

        for section in self.data.values():
            if isinstance(section, dict):
                agents.update(section.keys())

        return sorted(agents)

    def list_sections(self):
        return VALID_SECTIONS