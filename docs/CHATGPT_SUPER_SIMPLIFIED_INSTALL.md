# Super simplified install guide for ChatGPT users only

Let ChatGPT handle the cloning and setup. You do not need to type Git commands.

Use the ChatGPT desktop app with **Work and file/Git tools available**. Connecting GitHub gives repository access; cloning also needs a place where ChatGPT can create and edit files. If your project only accepts uploads, use the [full installation guide](INSTALLATION.md#if-your-project-only-supports-uploads).

## 1. Connect GitHub inside ChatGPT

Install/open the [official ChatGPT desktop app](https://learn.chatgpt.com/docs/app) and sign in.

Open **Plugins**, find **GitHub**, and install/connect it. Follow the GitHub sign-in prompts and allow access to the repository you want to use. Your interface may call these connections Apps; use its GitHub connection option.

The study-system repository is private. Your GitHub account needs access from the owner before ChatGPT can read it. [Official plugin setup](https://learn.chatgpt.com/docs/plugins).

## 2. Create your school project

Create a project named something like **My School Workspace**. Start a **Work** chat in it with file and Git tools available. Allow the folder access needed for setup.

## 3. Paste this install prompt

```text
Use my connected GitHub account to clone this repository into a new,
separate folder for my school workspace:
https://github.com/roberto-ram/efficient-ai-study-system

Make the cloned folder the main/primary folder of this project.
If you cannot change that app setting, give me the exact steps.
Do not change any existing school folders.

Read AGENTS.md and START_HERE.md. Verify that you can read and save
files in the clone, then begin onboarding with no more than five
bundled questions. Help me with any additional Git sign-in needed.

This is the shared blank template. Help me create my own private
repository before pushing any personal course files. Do not push
my changes to the shared template.
```

If you already created your own private copy, replace the link with your repository link.

If ChatGPT asks you to attach the cloned folder, open **Edit project -> Add folder**, choose that folder, and select **Make primary**. That makes it the starting folder for new chats. [Official project-folder instructions](https://learn.chatgpt.com/docs/projects).

## 4. Give it your class materials

Attach your syllabus, lecture notes, objectives, rubrics, and other class resources. Paste:

```text
These are my class resources. I am taking COURSE_NAME this TERM.
My current goal is GOAL.

Organize everything in my study workspace, preserve the originals,
and use my instructor's objectives and assignment requirements first.
Create the course, unit, exam, and assignment folders that are needed.
Save my preferences, source references, progress, and next steps so
I can open a new chat without explaining everything again.
Ask only for information you still need.
```

Replace COURSE_NAME, TERM, and GOAL with your information. You can give it several classes at once.

## 5. Check that a new chat remembers the saved work

Tell ChatGPT: **"Save a checkpoint and verify the files were saved."**

Open a new chat in the same project and paste:

```text
Read AGENTS.md and START_HERE.md, restore the saved context for my
current course, and continue from the latest handoff.
```

It should recover your course and next step from the saved files. If it cannot, ask it to verify the primary folder and latest saved context.

For more detail or a setup problem, use the [full installation guide](INSTALLATION.md).
