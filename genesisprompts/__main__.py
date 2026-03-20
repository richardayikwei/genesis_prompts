# genesisprompts/__main__.py

import argparse
import questionary
from .genesis import Genesis


DEFAULT_AGENTS = ["chat", "copilot", "claude"]
SECTIONS = ["idea", "feature", "refactor"]


def main():
    parser = argparse.ArgumentParser(prog="genesis")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("add", help="Add a new prompt")

    args = parser.parse_args()

    if args.command == "add":
        run_add()
    else:
        parser.print_help()


# -------------------------
# ADD COMMAND
# -------------------------
def run_add():
    g = Genesis()

    # 1. Select agent
    agents = g.list_agents() or DEFAULT_AGENTS

    agent = questionary.select(
        "Choose AI agent:",
        choices=agents
    ).ask()

    if not agent:
        print("Cancelled.")
        return

    # 2. Select section
    section = questionary.select(
        "Choose section:",
        choices=SECTIONS
    ).ask()

    if not section:
        print("Cancelled.")
        return

    # 3. Enter prompt
    prompt = questionary.text(
        "Paste your prompt:"
    ).ask()

    if not prompt:
        print("Prompt cannot be empty.")
        return

    # 4. Save
    entry = g.add_prompt(section, agent, prompt)

    print(f"\n✅ Saved: {entry['id']}")


if __name__ == "__main__":
    main()