# Claude Instructions for `odoo-partner`

TMC Odoo 19.0 addon repository.

## Agent Working Conventions

Conventions for anyone (including AI assistants) working in this repo. They live here,
checked into git, so they travel across machines instead of depending on a local
assistant memory.

### Working environment — never touch production

- **Never connect to the production database or a production instance.** Work only
  against local instances: a prod dump restored into a local container is a local copy,
  not production. Run smoke tests in throwaway ephemeral containers.
- If a step seems to require touching production (a prod host/IP, real credentials),
  **stop and ask** instead of attempting it.

### Interaction language

- Reply to the user in **Spanish** in chat/prose.
- Keep code, inline comments, and commit messages in **English**.

### Code comments

- Inline comments (XML, Python, JS) must be **a single line**, in English, and explain
  _why_, not _what_.
- Keep them **short — under ~79 characters**.
- If a rationale genuinely needs paragraphs (e.g. a subtle test invariant), put it in
  the commit message or PR description, not in an inline block.

### Formatting

- Format touched files with the repo's own tooling, not an editor/global config:
  `pre-commit run prettier --files <paths>` for XML/JS/JSON/MD/YAML,
  `pre-commit run ruff-format --files <paths>` for Python.
- XML follows the OCA Prettier config (`prettier.config.cjs`, `printWidth: 88`,
  `@prettier/plugin-xml`); that pre-commit output is the source of truth.

### Translations

- When a change adds or edits a user-facing string (field label, help text, selection
  label, button, `_()` message, view text), check whether the module's `i18n/es_AR.po`
  needs updating and add or adjust the Spanish translation in the same change. The UI
  language is es_AR, so an untranslated new string shows in English.

### Commit authorship

- **Never** add AI attribution: no `Co-Authored-By: Claude`, no "Generated with Claude
  Code", no emoji footer. Commits are authored solely by the human.
- Follow the Odoo Git guidelines and the `[TYPE] summary` convention ([FIX], [IMP],
  [ADD], [REF], [MIG], [REM], [UPD]); imperative mood; one logical change per commit.
- When porting someone else's commit (cherry-pick / re-apply), preserve **their**
  authorship with `git commit --author="Name <email>"` and keep a
  `(cherry picked from commit <sha>)` line.
- Ask the user for confirmation — files to commit plus the proposed message — before
  creating any commit; amends and cherry-picks included.
