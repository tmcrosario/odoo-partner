import re

from odoo import api, exceptions, fields, models


class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    @api.constrains("dni")
    def _check_dni(self):
        for partner in self:
            # fullmatch, not `$`, so a trailing newline cannot slip through
            if partner.dni and not re.fullmatch(r"[0-9]{8}", partner.dni):
                raise exceptions.ValidationError(self.env._("Invalid DNI."))

    civil_status = fields.Selection(
        [
            ("single", "Single"),
            ("married", "Married"),
            ("divorced", "Divorced"),
        ]
    )

    birthdate = fields.Date()

    dni = fields.Char(string="DNI")
