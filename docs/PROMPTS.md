# Copy-paste prompts

Replace capitalized placeholders. Text in code blocks is ready to paste into your AI.

## 1. Install and open the system

ChatGPT users can use the dedicated [super simplified guide](CHATGPT_SUPER_SIMPLIFIED_INSTALL.md), including a ready-to-paste prompt with the template repository link.

Use this only in an AI tool that has file/Git access. A chat-only tool cannot clone a repository just because you ask.

```text
Clone YOUR_PERSONAL_REPOSITORY_URL into NEW_LOCAL_FOLDER, without changing
any existing school workspace. Verify this is my own private repository.
Read AGENTS.md and START_HERE.md in the clone. Help me attach this folder
as the primary project folder if the app supports it; otherwise give me
the exact steps. Do not claim you changed app settings unless verified.
Check file reading and writing, then begin onboarding. Ask at most five
bundled questions, and reuse information I already provided.
```

If you need the owner's blank template first, use `https://github.com/roberto-ram/efficient-ai-study-system` as the URL and add: "This is the shared template. Help me create my own private repository before pushing any personalized files." Access must already be granted.

### After cloning or opening the folder yourself

```text
This folder is my main school workspace. Read AGENTS.md and START_HERE.md.
Check access, then set up the study system for me. Keep saved context
portable between ChatGPT Work, Codex, and Claude. Ask only for missing
information, in no more than five bundled questions. Keep the shared
templates blank and create my courses from them.
```

## 2. Add your first course

```text
I am taking COURSE_NAME in TERM. My current goal is GOAL.
These are my syllabus, objectives, lectures, assignment instructions,
and reference materials: ATTACHED_FILES_OR_FOLDER.
Organize this course in the study system. Preserve all originals.
Index the sources, map official objectives, and identify missing
information. Create relevant units, exams, and assignments only as needed.
Save my course context and the next step so a new chat can continue.
```

### Fictional examples — adapt to your actual class

**Math**

```text
Set up College Algebra. Here are my syllabus and lecture notes.
I need help choosing the right method and checking my work.
Prepare an Exam 1 priority map from the supplied scope, then quiz
me one problem at a time. Track mistakes by method and prerequisite.
```

**History or writing**

```text
Set up World History. Here are the reading list and essay rubric.
Organize reading units and an essay assignment. Help me compare
sources and build supported arguments. Save citation locations
and unfinished decisions. Do not invent quotes or references.
```

**Healthcare**

```text
Set up my nursing course using these objectives and lectures.
Enable healthcare tutoring and progressive case studies.
Teach cause -> mechanism -> findings -> priority action -> evaluation.
Use course sources first and record where my clinical reasoning fails.
Keep actual clinical paperwork separate from fictional practice.
```

**Multiple classes or subdivisions**

```text
I have three courses listed in these syllabi. Create a separate course
folder for each, grouped by term. Within COURSE_NAME, use the instructor's
units and separate lecture, lab, and project work where needed.
Build a dashboard from confirmed deadlines. Do not invent dates.
```

## 3. Start a new chat

```text
Read AGENTS.md and START_HERE.md, then restore the saved context for
COURSE_OR_TASK. Tell me briefly where we left off and continue with
the next step. Load only relevant files. If anything needed is missing
or stale, identify it rather than guessing.
```

For a provider switch, open the same current folder (or upload the current files) and use this same prompt.

## 4. Everyday requests

- "Explain TOPIC from my course materials and show why each step happens."
- "Quiz me on EXAM, one question at a time. Focus on my recorded weak areas."
- "Give me a whiteboard concept map of TOPIC."
- "Compare TOPIC_A and TOPIC_B using the clues my course emphasizes."
- "Read this assignment rubric and help me plan the required work."
- "I have AVAILABLE_TIME before CONFIRMED_DEADLINE. Make a realistic plan."
- "Here are new lecture files. Index them and update only the affected work."
- "This correction matters for future sessions: CORRECTION. Save it with its source."

## 5. Save a checkpoint

```text
Save a checkpoint now: demonstrated progress, recurring errors,
completed outputs, pending inputs, and the exact next action.
Update the relevant task handoff and the root pointer. Verify the
files were saved. Do not copy the entire chat or push to Git.
```

## 6. Upload-only / manual mode

```text
You can read my uploaded files but cannot change my main folder.
Use the uploaded AGENTS.md and START_HERE.md. At each checkpoint,
provide updated files or paste-ready contents with exact filenames.
Tell me what I must save and which uploaded versions to replace.
Do not claim you saved to my computer or synchronized GitHub.
```
