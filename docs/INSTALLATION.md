# Beginner installation guide

You do not need programming knowledge. StudyNest is a folder of instructions and blank templates. GitHub holds a saved version online; your AI works with the copy you make available to it.

**Blank template:** [StudyNest](https://github.com/roberto-ram/studynest). The template is public. Anyone can view or copy it.

**Another way for ChatGPT users:** follow the [Super simplified install guide for ChatGPT users only](CHATGPT_SUPER_SIMPLIFIED_INSTALL.md). Connect GitHub in ChatGPT, create a project, and give ChatGPT the repository link and install prompt.

**Gemini users:** follow the [Super simplified install guide for Gemini users only](GEMINI_SUPER_SIMPLIFIED_INSTALL.md). Import your copy, then save updated context files yourself and load them into your next chat.

## 1. Choose how your AI will access files

| Your tool | Setup path | Who saves updated context? |
| --- | --- | --- |
| ChatGPT Work / Codex with local folder tools | Local folder, below | AI, after verifying write access |
| Claude with local folder access / Cowork | Claude local path, below | AI, after verifying write access |
| Claude Code | Claude Code path, below | AI, after verifying write access |
| Gemini website | [Gemini guide](GEMINI_SUPER_SIMPLIFIED_INSTALL.md) | Student saves updates and uploads current files |
| A project/chat that only accepts uploads | Manual upload path, below | Student downloads/saves and replaces files |

A GitHub connector, uploaded ZIP, or conversation memory alone does not prove the AI can change your local folder. The setup prompt checks capabilities.

## 2. Make your personal copy on GitHub

1. Create an account at [GitHub](https://github.com). Save your sign-in details in your usual password manager.
2. Open the [StudyNest template](https://github.com/roberto-ram/studynest). You do not need an invitation. Sign in to GitHub to create your own copy.
3. Click **Use this template -> Create a new repository**. Choose your own account as owner, name it something like `my-study-workspace`, and choose **Private**.
4. Create the repository. You now have your own blank copy. Add your course content here, not to the shared original.

This path is available to people with read access to a GitHub template. [GitHub's template instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) explain the buttons.

**Already cloned the owner's repository?** A clone retains that repository as its remote destination. Before adding personal content, use the AI prompt in [Maintenance](MAINTENANCE.md#personal-copy-and-git) to establish your own private destination. You can study locally while that is pending; do not push personal changes to the template.

## 3. Put the copy on your computer

The easiest route uses [GitHub Desktop](https://desktop.github.com).

1. Install it and sign in to the same GitHub account.
2. Open **your personal repository** in your browser.
3. Click **Code -> Open with GitHub Desktop**.
4. Choose a folder you can find again, such as `Documents/School/my-study-workspace`, and finish the clone.
5. Write down the full local folder path. It should contain `AGENTS.md`, `START_HERE.md`, `context`, and `templates`.

These clone steps are documented by [GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

If your AI already has Git tools and authenticated access, you may instead give it the installation prompt in [Prompts](PROMPTS.md#1-install-and-open-the-system). Replace `YOUR_PERSONAL_REPOSITORY_URL` and the destination. The prompt cannot bypass sign-in or private-repository access.

A **Download ZIP** copy can work for local study or manual uploads, but it does not establish Git synchronization.

## 4A. ChatGPT Work or Codex

1. Install the [official ChatGPT desktop app](https://learn.chatgpt.com/docs/app) and sign in.
2. Choose **Work** or **Codex** if available in your account.
3. Create/add a local project and attach your cloned study folder. In **Edit project**, use **Add folder**, then **Make primary** for the study folder. Start new study chats in that project.
4. For the initial setup, work in the local folder. If using a separate worktree later, ensure its memory changes are saved back to the main copy.
5. Paste the post-clone setup prompt from Prompts.

The primary folder supplies the working context. Conversation sync and local file access are separate; files on one computer are not automatically available on another. [Official project guidance](https://learn.chatgpt.com/docs/projects).

Codex uses `AGENTS.md` for project guidance; the setup prompt also explicitly points to it. [Official AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## 4B. Claude with local folder access

1. Install Claude from the official download link in [Claude's local-project guide](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork), then sign in.
2. Find Projects and create a project using **an existing folder on your computer**. Select your cloned study folder.
3. Add the project instructions from `AGENTS.md`, then paste the post-clone setup prompt.
4. Let it verify file reading and writing before relying on saved progress.

Claude's interface is changing: some accounts show Cowork; others show a combined Claude experience. The linked guide explains the rollout and local-folder setup.

## 4C. Claude Code

1. Use the official installer linked from [Claude Code Desktop](https://code.claude.com/docs/en/desktop).
2. Sign in, open the **Code** tab, and start a **Local** session with your study folder selected.
3. Choose the permission mode appropriate for the work, then paste the post-clone setup prompt.
4. Keep `CLAUDE.md`: it imports the shared `AGENTS.md` rules, avoiding two independently maintained instruction sets. [Claude's memory documentation](https://code.claude.com/docs/en/memory).

You can use a coding agent for organizing and tutoring without turning this into a programming course.

## 5. Permissions and Git access

Allow your chosen tool to read and write the study folder. Approve Git/network actions when you ask it to clone or back up. Sign in through the provider's GitHub connection or GitHub Desktop when required; never paste a token into your course files.

Permission labels vary. Full access is optional, not a setup requirement; it grants broader autonomy than reading and editing this study folder. Use the provider controls that let it complete the actual task. [OpenAI permissions](https://learn.chatgpt.com/docs/permission-modes), [Claude Code permission modes](https://code.claude.com/docs/en/desktop#choose-a-permission-mode).

## 6. Add your classes

1. Tell the AI your course names and the kind of help you want.
2. Attach/drop in the syllabus, objectives, lecture files, rubrics, and assigned references, or tell it where those files already live.
3. Paste the course setup prompt from Prompts. It asks only for missing information, creates course folders, preserves originals, and saves context.
4. Check its course list, priorities, and missing information. Correct anything it misunderstood.

Examples for different subjects are included in Prompts. The system automatically enables healthcare case support when your supplied course information clearly warrants it.

## 7. Verify that a new chat can resume

Ask it to save a checkpoint. Start a new chat in the **same project/folder** and paste the resume prompt. It should recover the course, source priorities, demonstrated weaknesses, and next step from files. This tests your installation; it does not rely on a promise of perfect recall.

## If your project only supports uploads

Create a project in your chosen AI service. Paste `AGENTS.md` into project instructions where supported. Upload `START_HERE.md`, the four context files, the selected course README/Source Index/Progress/Handoff, the relevant workflow, and needed sources.

For Claude Projects, instructions and project knowledge are configured in the project interface. [Official project setup](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

Use the manual-mode prompt in Prompts. After changes, save the generated files to your personal copy and replace old uploaded versions. Future chats need the latest versions; an answer in one chat is not a saved update. If the tool cannot create files, ask for paste-ready contents per filename.

You can move to folder access later without changing your course structure.

## Common setup problems

| Problem | What to do |
| --- | --- |
| Private repository is unavailable | Sign in; verify access with its owner |
| AI cannot find START_HERE.md | Attach the correct folder or upload the file |
| AI reads files but cannot save | Enable writing for this folder, or use manual mode |
| New chat knows old information | Confirm folder/branch and latest saved files; replace stale uploads |
| Different device lacks textbooks | Restore ignored originals from your private backup |
| AI starts asking everything again | Use the resume prompt and make it read the saved context |
| Git wants to push to the owner's repository | Stop the push; set up your own private repository |
