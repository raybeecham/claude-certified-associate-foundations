# Scripts

## Validate content

```bash
python scripts/check_content.py
```

Checks:

- seven module directories;
- required module files;
- 56 question records;
- 84 flashcard records;
- answer and distractor structure;
- unique IDs; and
- local Markdown links.

## Publish the repository

Bash:

```bash
./scripts/publish.sh
```

PowerShell:

```powershell
.\scripts\publish.ps1
```

The scripts require the GitHub CLI and an authenticated session. They initialize Git when needed, commit the repository, create a public GitHub repository, add the remote, and push.

Pass a different repository name:

```bash
./scripts/publish.sh my-claude-study-guide
```

```powershell
.\scripts\publish.ps1 -RepoName my-claude-study-guide
```
