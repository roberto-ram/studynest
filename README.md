# Version 1.0 Efficient Ai study system

An adaptable school workspace for ChatGPT Work, Codex, Claude, and other AI tools that can read files.

Your courses, sources, study priorities, progress, and next steps live in this folder. A new chat can pick up from saved context instead of requiring you to explain everything again.

**Version 1.0.0 — private template repository.** Create your own private copy before adding coursework.

## Start here

**ChatGPT users:** try the [Super simplified install guide for ChatGPT users only](docs/CHATGPT_SUPER_SIMPLIFIED_INSTALL.md) to connect GitHub and let ChatGPT handle the clone and project setup.

1. Follow the [beginner installation guide](docs/INSTALLATION.md).
2. Copy the [setup prompt](docs/PROMPTS.md#1-install-and-open-the-system).
3. Add your class materials and use the [course setup prompt](docs/PROMPTS.md#2-add-your-first-course).
4. Open a fresh chat and try the [resume prompt](docs/PROMPTS.md#3-start-a-new-chat).

If your AI cannot write files, use the manual-save instructions in the installation guide. A chat saying it remembers something is not proof that the folder was updated.

## What the system does

- Keeps multiple classes, units, exams, and assignments separate.
- Builds study priorities from your instructor's objectives and rubrics.
- Explains why, quizzes you one question at a time, and targets weak reasoning.
- Saves demonstrated progress, corrections, preferences, and a clear next step.
- Adds clinical case-study support when a course is identified as healthcare.
- Reads small context files first, then only relevant material.
- Supports provider changes through plain Markdown rather than proprietary memory.

## Folder guide

| Location | Purpose |
| --- | --- |
| [START_HERE.md](START_HERE.md) | AI entry point and task routing |
| [context/](context/README.md) | Student profile, course registry, durable memory, latest handoff |
| [courses/](courses/README.md) | Your courses; empty in this shared version |
| [inbox/](inbox/README.md) | Temporary arrival point for new materials |
| [templates/](templates/README.md) | Blank course, exam, unit, assignment, and progress templates |
| [workflows/](workflows/README.md) | Onboarding, source intake, study, exams, assignments, progress |
| [modules/](modules/README.md) | Optional subject-specific guidance |
| [docs/](docs/README.md) | Installation, copy-paste prompts, maintenance, and design |

Read the [design](docs/DESIGN.md) to see how it works. See the [release checklist](docs/REVIEW.md) for validation and maintenance.

## What is included

Blank instructions and templates, plus clearly labeled fictional setup prompts. No actual students, classes, textbooks, lectures, grades, patient records, or previous chat transcripts are included.

The system requires no paid API, database, plugin, or programming runtime. Your chosen AI service may have its own access requirements. Optional checks use Python 3.9 or later.

Personalization changes your own copy. Keep the shared template blank. Copying files does not automatically sync them to GitHub or Google Drive.
