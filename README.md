# StudyNest

Keep your classes, study materials, and next steps in one place.

StudyNest is a blank study workspace for ChatGPT Work, Codex, Claude, and other AI tools that can read files. It saves your course context in the folder so a new chat can pick up where you left off.

**Version 1.0.1. Public template.** Make your own private copy before adding personal coursework.

## Get started

**ChatGPT users:** use the [Super simplified install guide for ChatGPT users only](docs/CHATGPT_SUPER_SIMPLIFIED_INSTALL.md).

For other setups:

1. Follow the [installation guide](docs/INSTALLATION.md).
2. Paste the [setup prompt](docs/PROMPTS.md#1-install-and-open-the-system).
3. Add your class materials with the [course setup prompt](docs/PROMPTS.md#2-add-your-first-course).
4. Try the [resume prompt](docs/PROMPTS.md#3-start-a-new-chat) in a fresh chat.

If your AI cannot edit the folder, the guide shows you how to save updated files yourself.

## What you can do

- Organize classes into units, exams, and assignments.
- Study from your instructor's objectives and rubrics.
- Practice one question at a time and get help with mistakes.
- Save preferences, progress, and unfinished work for your next session.
- Use progressive clinical cases for healthcare courses.
- Switch AI tools while keeping your saved files.

The AI starts with a few short context files and reads the course material needed for the task. This avoids loading every class and document into each chat.

## Find your files

| Folder or file | What's there |
| --- | --- |
| [START_HERE.md](START_HERE.md) | Where the AI starts |
| [context/](context/README.md) | Your preferences, course list, saved decisions, and last task |
| [courses/](courses/README.md) | Your courses, empty until setup |
| [inbox/](inbox/README.md) | New materials waiting to be organized |
| [templates/](templates/README.md) | Blank course, exam, unit, and assignment files |
| [workflows/](workflows/README.md) | Instructions for tutoring and organizing work |
| [modules/](modules/README.md) | Subject guidance, including healthcare |
| [docs/](docs/README.md) | Setup guides, prompts, and maintenance |

The [design notes](docs/DESIGN.md) explain how saved context works. The [release checklist](docs/REVIEW.md) covers template maintenance.

## Before you add coursework

This repository contains blank templates and fictional setup examples. It includes no real student records, course uploads, grades, or patient data.

You do not need an API key, database, or programming tools to use StudyNest. Your AI service may have its own account requirements. The optional file checker needs Python 3.9 or later.

Keep personal work in your own private copy. Saving a local file does not automatically back it up to GitHub or Google Drive.
