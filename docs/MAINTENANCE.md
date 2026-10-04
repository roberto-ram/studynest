# Save, sync, and recover

Local file updates are part of normal study work. Git pushes, external backups, reminders, and submissions require a student request; file saving and cloud synchronization are different actions.

## Personal copy and Git

The shared template stays blank. Students should create their own private repository before personalizing and pushing.

If a student cloned the template directly, use this prompt:

```text
Check this folder's Git remotes and repository owner without exposing
credentials. Help me create my own private repository and use it as this
folder's push destination. Keep the blank template separate. Preserve
existing files and history; do not delete folders or overwrite remote work.
Show and verify the resulting destination before backing up personal files.
```

Before a requested push:

1. Verify the exact folder, branch, remote, ownership, and private visibility.
2. Review changed files and exclusions. Do not push personal context to the shared template.
3. Commit only intended changes, push to the verified destination, and verify the remote commit.
4. Say exactly what was synchronized and what was excluded. Never change visibility automatically.

Profile, course progress, handoffs, and Markdown notes are eligible for Git tracking in a student's own repo. `sources/`, `inbox/`, `outputs/`, `workfiles/`, and `archive/` contents are excluded by default. Adding new file types elsewhere may still track them, so inspect the staged files.

## Originals and outputs

Use an appropriate private backup, such as the student's own storage, for excluded materials. Do not assume a source link is a backup. Respect course sharing restrictions and use de-identified clinical data when applicable.

Git history can retain previously committed files even after a later deletion or ignore rule. Do not use the template repository as a personal archive.

## Switch AI or computer

1. Save the current task state and verify the files.
2. Synchronize the student's own repo if requested.
3. On the destination, restore the latest copy and any needed excluded originals.
4. Open that folder or upload current context files.
5. Use the resume prompt and confirm the recovered state.

Keep provider-specific auto-memory optional; necessary facts belong in the portable files.

## Maintenance and recovery

Reconcile stale deadlines and superseded facts. Compact repeated practice logs while preserving evidence and unresolved errors. Archive only when requested; do not delete student work automatically.

If the working copy differs from cloud data, preserve both and compare before resolving. For unreadable or missing sources, mark the gap and request the needed material. For a fresh chat that ignores saved context, explicitly make it read START_HERE.md and the selected task handoff.

If optional Python is available, run `python tools/validate_workspace.py` from this folder. This checks structure and local document links, not AI accuracy or clinical correctness.
