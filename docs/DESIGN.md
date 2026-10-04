# Version 1.0 design

The durable context is the student's folder. Provider memory can help, but it is not the only copy of course priorities, preferences, and progress.

## Layers

| Layer | Holds | Read when |
| --- | --- | --- |
| Shared rules | AGENTS.md; CLAUDE.md imports it | Session start |
| Small personal context | Profile, dashboard, memory, latest pointer | Session start |
| Course context | README, source index, progress | Selected course |
| Task context | Exam map, assignment brief, unit or task handoff | Selected task |
| Original evidence | Lecture pages, objectives, rubric, assigned readings | Needed for a claim |
| Optional domain guidance | Healthcare or subject adaptation | Enabled/relevant only |

A new chat reads the short entry point, selects a course, resumes its task, and retrieves only the evidence needed. This reduces unnecessary context loading; actual tokens and cost depend on the provider, tools, and request.

## What carries forward from a strong study workspace

- Instructor-first source priority and explicit source conflicts.
- Course/exam folders with smaller lecture or unit subdivisions.
- Objective-based priority maps.
- Explain-why teaching, comparisons, whiteboard summaries, and adaptive quizzes.
- Assignment workflows that preserve blank forms and original references.
- Progressive healthcare cases where appropriate.
- Clinical-judgment reasoning as a healthcare module.
- Saved progress and next steps.

Course names, proprietary uploads, real grades, patient records, personal reflections, and historical chat content stay out of the blank template.

## What is generalized

A clinical teaching sequence becomes a general reasoning sequence with subject-specific adaptations. Clinical priorities and medication/lab formats load only for healthcare. Other disciplines can use their own case/problem formats.

Templates are copied when needed. One student may have a single course; another may group several programs by term. Exact paths are registered in the dashboard rather than hard-coded in global instructions.

## Memory that stays useful

Preferences need student evidence. Course facts need sources. Progress needs observed responses. The system stores these separately and replaces superseded corrections.

Current summaries stay small; detailed older work is linked rather than reread. Handoffs are saved during meaningful checkpoints so reopening a chat does not depend solely on an end-of-session command.

"Always learning" means updating supported preferences, corrections, and demonstrated learning evidence. It does not mean training a model, guaranteeing perfect recall, or predicting grades.

## Ownership and portability

The owner maintains a blank template. Students create their own private copies, personalize those, and choose backups for their originals. A private template needs access invitations before other people can copy it.

Plain Markdown is the common interface. Codex follows AGENTS.md; Claude Code imports it through CLAUDE.md; upload-only projects receive instructions and updated files manually. The [installation guide](INSTALLATION.md) links the current provider instructions.

A cloud chat sees only files available to that environment. Ignored originals and unsaved local changes will not appear just because GitHub is connected.

## Scope of Version 1.0

Included: folders, templates, instructions, setup prompts, source indexing, progress, handoffs, subject activation, and maintenance.

Deferred: LMS scraping, grade integrations, calendar sync, automatic reminders, cross-device sync services, and app-specific extensions. They can be added deliberately when a student actually needs them.
