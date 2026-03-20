# genesisprompts/__main__.py

import argparse
import questionary
from .genesis import Genesis


DEFAULT_AGENTS = ["chat", "copilot", "claude"]
SECTIONS = ["idea", "feature", "refactor"]


def main():
    parser = argparse.ArgumentParser(
        prog="genesis",
        description="Genesis Prompts CLI - Track and manage AI prompts for your projects",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Commands",
        metavar=""
    )

    # -------------------------
    # ADD COMMAND
    # -------------------------
    subparsers.add_parser(
        "add",
        help="Add a new prompt",
        description="Interactively add a prompt to the .prompts file"
    )

    # -------------------------
    # FUTURE COMMANDS (placeholder)
    # -------------------------
    subparsers.add_parser(
        "list",
        help="List stored prompts (coming soon)"
    )

    args = parser.parse_args()

    if args.command == "add":
        run_add()
    elif args.command == "list":
        print("🚧 'list' command coming soon")
    else:
        parser.print_help()


# -------------------------
# AGENT SELECTION
# -------------------------
def select_agent(genesis: Genesis):
    existing_agents = genesis.list_agents()
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
# ADD FLOW
# -------------------------
def run_add():
    g = Genesis()

    agent = select_agent(g)
    if not agent:
        return

    section = questionary.select(
        "Choose section:",
        choices=SECTIONS
    ).ask()

    if not section:
        print("Cancelled.")
        return

    prompt = questionary.text(
        "Paste your prompt:"
    ).ask()

    if not prompt or not prompt.strip():
        print("Prompt cannot be empty.")
        return

    entry = g.add_prompt(section, agent, prompt)

    print(f"\n✅ Saved: {entry['id']}")


if __name__ == "__main__":
    main()