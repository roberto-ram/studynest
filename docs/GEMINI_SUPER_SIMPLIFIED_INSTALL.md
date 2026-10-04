# Super simplified install guide for Gemini users only

Use StudyNest in the Gemini website without typing Git commands. You will import the template, add your classes, and save updated files for your next chat.

Gemini's GitHub import reads a snapshot. It cannot save changes back to your repository or keep that snapshot synchronized. This guide uses a personal folder where you save the updates Gemini provides. [Google's GitHub guide](https://support.google.com/gemini/answer/16176929?hl=en).

## 1. Make your own copy

1. Create or sign in to your account at [GitHub](https://github.com).
2. Open [StudyNest](https://github.com/roberto-ram/studynest).
3. Click **Use this template -> Create a new repository**. Choose your account, name the repository something like `my-study-workspace`, select **Private**, and create it.
4. In your new repository, click **Code -> Download ZIP**. Extract the ZIP into a folder you can find, such as `Documents/School/My StudyNest`.
5. Open that folder. Check that it contains `AGENTS.md`, `START_HERE.md`, `context`, and `templates`. Keep this folder as your main saved copy.

The private repository starts with the blank template. Saving files in the extracted folder does not update GitHub. You can set up backups later using [Maintenance](MAINTENANCE.md).

## 2. Import your copy into Gemini

1. On a computer, open [Gemini](https://gemini.google.com) and sign in with your Google account. No desktop app is needed for this setup.
2. Start a new chat.
3. Click **Add file -> More uploads -> Import code**.
4. Paste the link to **your private repository** and click **Import**.
5. Follow the sign-in steps to link GitHub if prompted. Use the account that owns your copy.

You must use the import button; pasting the link into a normal chat does not load the repository. [Google's import instructions](https://support.google.com/gemini/answer/16176929?hl=en).

## 3. Paste this setup prompt

```text
Use the attached StudyNest files as my study system.

Read AGENTS.md and START_HERE.md, then the four context files named
there. Follow those instructions and begin onboarding with no more
than five bundled questions. Do not load every course or source.

I am using the Gemini website. Treat this as manual-save mode.
Do not claim you can edit my computer folder, update GitHub, or
make the repository a writable project folder.

When files need updating, provide the complete updated contents
and exact relative filename for each file. Provide downloadable
files if available; otherwise give me copy-and-save instructions.
Preserve original source materials and save useful context in the
StudyNest files instead of relying on chat memory.

If required files are missing or unreadable, name them before
continuing. Do not guess their contents.
```

## 4. Add your class resources

Use **Add files -> Upload files** to attach your syllabus, objectives, lecture notes, assignment instructions, and relevant readings. Add materials in small batches if needed. [Google's file-upload instructions](https://support.google.com/gemini/answer/14903178?hl=en).

Paste this prompt, replacing the words in capitals:

```text
These are my resources for COURSE_NAME during TERM.
My current goal is GOAL.

Use my instructor's materials, objectives, and rubrics first.
Propose a course folder structure using the StudyNest templates.
Provide the initial course README, Source Index, Progress, and
Handoff, plus any changed root context files, with exact paths.
Tell me where to save each original resource without altering it.
Create only the unit, exam, and assignment sections I need.

Ask only for missing information. Do not invent deadlines, grades,
mastery, or source details. Explain how to save the resulting files
in my personal folder because this chat cannot write there.
```

Examples you can give:

- **Nursing:** "I am starting OB. Use my syllabus and lecture objectives to plan the next exam and practice clinical judgment."
- **Chemistry:** "Help me organize each unit, work through calculations, and track mistakes from practice."
- **History:** "Organize weekly readings and essay rubrics. Help me build arguments using the assigned sources."

For healthcare courses, the shared instructions enable the healthcare module and a case-study section when your course information supports it.

Create the folders Gemini lists inside your personal StudyNest folder. Save each generated file at its stated path. Keep your original class resources in the specified course `sources` folder.

## 5. Save your progress after studying

Paste:

```text
Prepare a StudyNest checkpoint. Provide complete updated versions
of only the files that changed, with their exact paths. Include
confirmed preferences, observed practice results, unresolved
questions, and my next step. Update the root handoff so a fresh
chat can find the current course and task.

Give me a short save checklist. Mark these files as proposed
updates until I have saved them. Do not claim they are on disk.
```

Download each file if Gemini offers a download, then place it at the listed path in your personal folder. Check the name so it replaces the intended file instead of leaving a second copy such as `HANDOFF (1).md`.

If Gemini provides only text, open the existing file in a plain text editor, replace its contents with the complete update, and save. For a new file in Windows Notepad, choose **Save as type: All files**, use the exact filename including `.md`, and select UTF-8. Do not include the surrounding chat code fences.

Open the saved files once to check them. The saved files are what your next chat will use.

## 6. Start a fresh chat with your latest files

Your original GitHub import still contains the earlier snapshot. After local changes, load your updated personal folder instead.

1. Start a new Gemini chat on a computer.
2. Choose **Add file -> More uploads -> Import code -> Upload folder**, and select the saved StudyNest folder. Upload the needed class resources separately if they were not included or readable.
3. Paste the resume prompt below.

Google documents folder import and upload limits. If your folder is too large or rejected, use the smaller upload list below. [Google's folder and file-upload guide](https://support.google.com/gemini/answer/14903178?hl=en).

```text
Read AGENTS.md and START_HERE.md from the attached current files.
Restore my context, then read the selected course and task files.
Tell me the current course, my last confirmed progress, and the
next step from the saved handoff. Continue in manual-save mode.
If a needed file is missing, identify it instead of guessing.
```

Check that Gemini identifies the next step you just saved. If it reports an older task, check that you uploaded your latest folder.

## If Import code is unavailable

GitHub import has account requirements, including age 18 or over and Keep Activity enabled. School accounts also depend on their organization's settings. Check [Google's requirements](https://support.google.com/gemini/answer/16176929?hl=en) if the option is missing.

Use regular file uploads instead. Start with these six files from your extracted folder:

- `AGENTS.md`
- `START_HERE.md`
- `context/STUDENT_PROFILE.md`
- `context/DASHBOARD.md`
- `context/MEMORY.md`
- `context/HANDOFF.md`

Next, upload the selected course README, Source Index, Progress, and Handoff, the relevant workflow, and the needed class resources in additional batches. Tell Gemini each file's folder path if an upload shows only its filename. Use the same setup or resume prompt.

If a Markdown file is rejected, upload a temporary `.txt` copy and state its original path. Keep the original `.md` file in your personal folder. Replace outdated attachments when starting a new chat.

For direct reading and saving in a local folder, Gemini CLI is a separate option with more setup. It supports project instructions through `GEMINI.md`. [Official Gemini CLI setup](https://geminicli.com/docs/get-started/installation/), [project context](https://geminicli.com/docs/cli/gemini-md/).

Instructions checked against Google's documentation on October 4, 2026. This guide has not been tested in a live student Gemini account.
