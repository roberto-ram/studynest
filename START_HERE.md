# AI session entry point

Read once at session start:

1. [Student profile](context/STUDENT_PROFILE.md).
2. [Dashboard](context/DASHBOARD.md): course paths, confirmed deadlines, and active focus.
3. [Durable memory](context/MEMORY.md).
4. [Latest handoff](context/HANDOFF.md).

If setup is incomplete, use [onboarding](workflows/ONBOARDING.md). Otherwise choose the course/task named in the user's request. A user's new request overrides the last focus. For "continue," resolve the handoff; ask only if the target is ambiguous.

Read the chosen course README, its Source Index, and current Progress. For exam work, also read that exam's Priority Map and README. For assignments, read that assignment's brief and rubric references. Follow the local handoff for that task; the root handoff is only a pointer.

Load exactly one relevant workflow:

| Task | Workflow |
| --- | --- |
| Add course materials | [Source intake](workflows/SOURCE_INTAKE.md) |
| Explain, compare, quiz, concept map | [Study](workflows/STUDY.md) |
| Exam plan, guide, review | [Exams](workflows/EXAMS.md) |
| Homework, essay, project, lab report | [Assignments](workflows/ASSIGNMENTS.md) |
| Save, resume, progress, review planning | [Progress](workflows/PROGRESS.md) |

Load only the domain modules listed in the selected course README. [Module selection](modules/README.md) governs healthcare activation.

Retrieve relevant pages/sections from source files on demand. Reuse verified extracts if the original file has not changed. Do not read every course, template, source, or old session. Large files belong behind indexes, not in startup memory.

Before closing a task, save its state and update the root pointer. Follow [maintenance](docs/MAINTENANCE.md) only for sync, Git, archiving, or recovery.
