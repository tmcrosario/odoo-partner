# Migration Notes — odoo-partner (14.0 → 19.0)

Repo contains two modules: `partner_fiscal` and `partner_tmc`.

## Summary of changes by category

### Models

- No changes required. Both `partner_fiscal/models/partner.py` and
  `partner_tmc/models/partner.py` already use the modern API (`@api.constrains`,
  `fields.*`, `odoo.exceptions`). No `name_get`, `fields_view_get`,
  `@api.one/@api.multi`, `read_group`, `_sql_constraints`, `track_visibility`, or
  `_cr/_uid/_context` usages found.

### Views

- `partner_tmc/views/partner.xml`: converted the one deprecated `attrs` (removed in
  17.0):
  - `attrs="{'invisible': [('is_company','=',True)]}"` → `invisible="is_company"`
    (single-tuple, truthy on a boolean field — straightforward; not a compound domain).
- `partner_fiscal/views/partner.xml`: no changes (no `attrs`/`states`/`<tree>`).
- No `<tree>`, `states=`, `t-esc`, `tree_view_ref`, `oe_chatter`, or `view_mode` tree
  refs in this repo.

### Security

- No security/ files in this repo.

### Tests

- None present.

### Manifests

- `partner_fiscal`: version `14.0.1.0.0` → `19.0.1.0.0`; removed dead `"qweb": []` key
  (deprecated); **added `"base"` to `depends`** — the view inherits
  `base.view_partner_form`, so `base` was an undeclared (implicit) dependency. License
  already `AGPL-3`.
- `partner_tmc`: version `14.0.1.0.0` → `19.0.1.0.0`; removed dead `"qweb": []` key.
  `depends` unchanged (`partner_firstname`, `base_address_extended`, `partner_fiscal`).

## 18.0 branch

- None existed for this repo. Branch `19.0` created fresh from `14.0`.

## Removed dependencies

- None removed.

## Dependencies to verify before push

- `partner_firstname` — OCA partner-contact module; verify a 19.0 release exists.
- `base_address_extended` — Odoo core (community) module; verify it still ships in 19.0
  core.

## Autosave / onchange → constrains conversions

- None. The repo has no `@api.onchange` methods; validations are already in
  `@api.constrains` (`_check_cuit`, `_check_dni`), which is the correct, autosave-safe
  pattern for 19.0.

## Items left for human review

- `partner_tmc/models/partner.py` and `partner_fiscal/models/partner.py` both set
  `_name = "res.partner"` together with `_inherit = "res.partner"`. This redundant
  pairing is a legacy style (the modern idiom is `_inherit` only). It is harmless and
  not a 19.0 breakage, so it was left untouched to avoid an unjustified change. Consider
  dropping the `_name` line later.

## Lint findings

pre-commit ran fully (ruff, prettier, pylint-odoo, odoo-pre-commit-hooks). Auto-fixers
(ruff, ruff-format, prettier) were applied. Remaining reporter findings (non-blocking,
follow-ups):

- `manifest-required-author` (both modules): pylint-odoo's OCA rcfile requires the
  author "Odoo Community Association (OCA)". These are private TMC modules, not OCA
  addons — expected and intentionally not changed.
- `prefer-env-translation` (`partner_fiscal/models/partner.py:_check_cuit`,
  `partner_tmc/models/partner.py:_check_dni`): Odoo 19.0 prefers `self.env._(...)` over
  the module-level `_`. A valid future cleanup; left as-is this round (still works).
- A few `unknown-option-value` warnings come from the canonical OCA `.pylintrc` listing
  message names not present in this pylint-odoo version — harmless, kept the canonical
  file verbatim.

Note: `python -m py_compile` and `ruff`/`xmllint` validate syntax/format only, NOT Odoo
runtime API correctness — real API validation is deferred to the boot/test stage.

## Tooling

- Added the canonical OCA 19.0 pre-commit stack (ruff + ruff-format + prettier +
  eslint + pylint-odoo + odoo-pre-commit-hooks), adapted for a non-OCA private repo by
  dropping the OCA-publishing-only hooks (whool, maintainer-tools
  readme/website/excluded-addons generators). Companion files: `.pylintrc`,
  `.pylintrc-mandatory`, `prettier.config.cjs`, `eslint.config.cjs`, `.editorconfig`,
  `pyproject.toml` (ruff config). Existing `.gitignore` was kept.

## Translations

- Translation regeneration deferred to a later stage.
