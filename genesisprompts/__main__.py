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
# AGENT SELECTION
# -------------------------
def select_agent(genesis: Genesis):
    existing_agents = genesis.list_agents()

    # merge default + existing agents
    all_agents = sorted(set(existing_agents + DEFAULT_AGENTS))

    agent = questionary.select(
        "Choose AI agent:",
        choices=all_agents + ["+ Add new agent"]
    ).ask()

    if not agent:
        print("Cancelled.")
        return None

    if agent == "+ Add new agent":
        agent = questionary.text("Enter new agent name:").ask()

        if not agent:
            print("Cancelled.")
            return None

    return agent.strip().lower()


# -------------------------
# ADD COMMAND
# -------------------------
def run_add():
    g = Genesis()

    # 1. Agent selection (fixed)
    agent = select_agent(g)
    if not agent:
        return

    # 2. Section selection
    section = questionary.select(
        "Choose section:",
        choices=SECTIONS
    ).ask()

    if not section:
        print("Cancelled.")
        return

    # 3. Prompt input
    prompt = questionary.text(
        "Paste your prompt:"
    ).ask()

    if not prompt or not prompt.strip():
        print("Prompt cannot be empty.")
        return

    # 4. Save
    entry = g.add_prompt(section, agent, prompt)

    print(f"\n✅ Saved: {entry['id']}")


if __name__ == "__main__":
    main()