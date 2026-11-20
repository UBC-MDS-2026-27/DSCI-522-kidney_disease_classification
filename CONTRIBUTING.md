# Contributing

Thanks for your interest in our chronic kidney disease classification project! We welcome bug reports, improvements to the analysis, and fixes to the documentation from anyone. By taking part, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting a bug

First, search the [existing issues](https://github.com/UBC-MDS-2026-27/DSCI-522-kidney_disease_classification/issues) to see whether the problem has already been reported. If not, open a new issue that includes:

- what happened, and what you expected to happen;
- the steps we can follow to reproduce the problem;
- your operating system (e.g., macOS 15 or Windows 11); and
- the command that failed, with its full error message pasted as text.

## Suggesting a change

Before starting work on a new idea, open an issue that describes the change and explains why it would help the project. This lets the team discuss it first, so that no effort is wasted on a change that does not fit or that someone else is already making.

## Submitting your work

1. Team members create a branch in this repository; outside contributors fork the repository first. Use a name that describes the work, such as `fix-readme-usage`.
2. Keep each branch to one small, focused change, and write commit messages that say what changed (e.g., `Add boxplot of hemoglobin by class`).
3. Edit the Quarto source file (`.qmd`), not the rendered HTML.
4. Open a pull request into `main` that explains your change and links its issue with `Closes #N`.
5. At least one team member must review and approve the pull request before it is merged. Nobody pushes directly to `main`.

## Setting up the project

Follow the instructions in the [Usage section of the README](README.md#usage) to create the environment and render the report. If your change needs a new Python package, add it with `uv add <package>` rather than `pip install`, and commit the updated `pyproject.toml` and `uv.lock` together so that everyone can reproduce the same environment.

## AI policy

You may use generative AI tools (e.g., ChatGPT, Claude, or Copilot) to help write or debug code, draft text, or explain errors. If you do:

- **Disclose it.** Say in your pull request description which tool you used and what for. Significant AI use is also recorded in the AI use statement in our [README](README.md).
- **Take responsibility for it.** You are fully responsible for everything you submit. Read, test, and understand any AI-generated code or text before submitting it, and make sure you can explain it to a reviewer. Check that every reference is real and supports the claim it is cited for; AI-invented citations are not accepted.
- **Keep humans in charge.** Issues and pull requests are opened, reviewed, and merged by people, never by an AI agent or chat bot. AI tools may help check code before merging, but they never approve or merge a pull request.

## Attribution

This guide was written by our team for the DSCI 522 course at the University of British Columbia.