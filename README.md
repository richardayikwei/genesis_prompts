# Genesis Prompts

A CLI tool for logging AI prompts to track the evolution of a project and provide evidence of authorship when building with AI.

---

## Compatability

Compatable with python >= 3.10

---

## Why Genesis Prompts?

When building with AI, a key question arises:

> *Who owns what is produced?*

Genesis Prompts helps you:

* Track the prompts used to build your project
* Maintain a structured history of development
* Provide proof of authorship and intent
* Reproduce how a system was created

---

## Usage

### Add a prompt

```bash
uv run genesis add
```

Or (if your virtual environment is activated):

```bash
genesis add
```

---

### Interactive flow

You will be prompted to:

1. Select AI agent (arrow keys)
2. Select section:

   * idea
   * feature
   * refactor
3. Paste your prompt

Example:

```
Choose AI agent:
> chat
  copilot

Choose section:
> feature

Paste your prompt:
> Add authentication system

✅ Saved: feat-001
```

---

## Project Behavior

Genesis Prompts will:

* Automatically detect your project root (via `pyproject.toml`)
* Create a `.prompts` file if it does not exist
* Append entries in a structured, versioned format

---

## Genesis Prompts Format

### Overview

The `.prompts` file is a YAML-based format used to define and track AI prompts across the lifecycle of a project.

It organizes prompts into three main stages:

* Idea
* Feature
* Refactor

---

### Structure

#### 1. Idea

Captures the initial prompts that define the concept or starting point of a project.

#### 2. Feature

Contains prompts used to build and extend the project.

#### 3. Refactor

Contains prompts used to improve or restructure the project.

---

### Agent Grouping

Prompts are grouped by the AI agent used:

* `chat` (e.g., ChatGPT)
* `copilot` (e.g., GitHub Copilot)

---

### Prompt Entry

Each prompt includes:

* `id` → unique identifier
* `prompt` → the actual prompt text
* `created_at` → timestamp

---

### Example

```yaml
version: 1

idea:
  chat:
    - id: idea-001
      prompt: |
        Build a FastAPI app for managing users.
      created_at: 2026-03-20
```

---

## Help

Access help by using the commands

```bash
uv run genesis --help

or

genesis --help
```
---

## Running Tests

Run tests using:

```bash
pytest
```

Or with uv:

```bash
uv run pytest
```

---

## Development Setup

Install development dependencies:

```bash
uv sync --dev
```

---

## Versioning & Changelog

This project uses Commitizen for versioning:

```bash
cz commit
cz bump
```

---

## Contributing

Contributions are welcome.

1. Fork the repo
2. Create a branch
3. Make changes
4. Run tests
5. Submit a pull request

---

## License

MIT License

---

## Final Note

Genesis Prompts is not just a logging tool.

It is a system for:

* documenting AI-assisted development
* preserving intent
* proving authorship

As AI becomes more integrated into software development, tools like this become essential.
