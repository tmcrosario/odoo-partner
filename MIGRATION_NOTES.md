# Migration Notes — odoo-partner (14.0 → 19.0)

Repo contains two modules: `partner_fiscal` and `partner_tmc`.

## Summary of changes by category

### Models
- No changes required. Both `partner_fiscal/models/partner.py` and `partner_tmc/models/partner.py`
  already use the modern API (`@api.constrains`, `fields.*`, `odoo.exceptions`). No `name_get`,
  `fields_view_get`, `@api.one/@api.multi`, `read_group`, `_sql_constraints`, `track_visibility`,
  or `_cr/_uid/_context` usages found.

### Views
- `partner_tmc/views/partner.xml`: converted the one deprecated `attrs` (removed in 17.0):
  - `attrs="{'invisible': [('is_company','=',True)]}"` → `invisible="is_company"`
    (single-tuple, truthy on a boolean field — straightforward; not a compound domain).
- `partner_fiscal/views/partner.xml`: no changes (no `attrs`/`states`/`<tree>`).
- No `<tree>`, `states=`, `t-esc`, `tree_view_ref`, `oe_chatter`, or `view_mode` tree refs in this repo.

### Security
- No security/ files in this repo.

### Tests
- None present.

### Manifests
- `partner_fiscal`: version `14.0.1.0.0` → `19.0.1.0.0`; removed dead `"qweb": []` key (deprecated);
  **added `"base"` to `depends`** — the view inherits `base.view_partner_form`, so `base` was an
  undeclared (implicit) dependency. License already `AGPL-3`.
- `partner_tmc`: version `14.0.1.0.0` → `19.0.1.0.0`; removed dead `"qweb": []` key. `depends`
  unchanged (`partner_firstname`, `base_address_extended`, `partner_fiscal`).

## 18.0 branch
- None existed for this repo. Branch `19.0` created fresh from `14.0`.

## Removed dependencies
- None removed.

## Dependencies to verify before push
- `partner_firstname` — OCA partner-contact module; verify a 19.0 release exists.
- `base_address_extended` — Odoo core (community) module; verify it still ships in 19.0 core.

## Autosave / onchange → constrains conversions
- None. The repo has no `@api.onchange` methods; validations are already in `@api.constrains`
  (`_check_cuit`, `_check_dni`), which is the correct, autosave-safe pattern for 19.0.

## Items left for human review
- `partner_tmc/models/partner.py` and `partner_fiscal/models/partner.py` both set
  `_name = "res.partner"` together with `_inherit = "res.partner"`. This redundant pairing is a
  legacy style (the modern idiom is `_inherit` only). It is harmless and not a 19.0 breakage, so it
  was left untouched to avoid an unjustified change. Consider dropping the `_name` line later.

## Lint findings
- See the `[ADD]` tooling commit; pre-commit output captured there.

## Translations
- Translation regeneration deferred to a later stage.
