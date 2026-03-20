# Genesis Prompts
A CLI tool used to log prompts for the purpose of proving that you are the author of a work you built using AI

## Genesis Prompts Format

### Overview

The ```.prompts``` file is a YAML-based format used to define and track AI prompts across the lifecycle of a project.

It organizes prompts into three main stages:

    Idea

    Feature

    Refactor

This structure allows developers to document how a project evolves through AI-assisted development.

### Structure
1. Idea

The idea section captures the initial prompts that define the concept or starting point of a project.

These prompts typically describe:

    The problem being solved

    The initial system design

    The first implementation request

2. Feature

The feature section contains prompts used to build and extend the project.

These prompts typically:

    Add new functionality

    Expand existing capabilities

    Introduce new components or integrations

3. Refactor

The refactor section contains prompts focused on improving existing code.

These prompts typically:

    Improve code structure and readability

    Optimize performance

    Reduce complexity

    Apply best practices

Agent Grouping

Within each section, prompts are grouped by the AI agent used to generate them.

Examples:

    chat (e.g., ChatGPT)

    copilot (e.g., GitHub Copilot)

This allows tracking of:

    Which tool generated each prompt

    Differences in output across tools

Prompt Entries

Each prompt entry includes:

    id: Unique identifier for the prompt

    prompt: The actual prompt text

    created_at: Timestamp of when the prompt was created

Example

version: 1

idea:
  chat:
    - id: idea-001
      prompt: |
        Build a FastAPI app for managing users.
      created_at: 2026-03-20

Purpose

This format enables:

    Reproducibility of AI-generated work

    Prompt versioning and tracking

    Better collaboration and auditing

    Clear separation of development stages

