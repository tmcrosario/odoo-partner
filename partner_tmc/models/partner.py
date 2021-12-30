import re

from odoo import _, api, exceptions, fields, models


class Partner(models.Model):

    _name = "res.partner"
    _inherit = "res.partner"

    @api.constrains("dni")
    def _check_dni(self):
        pattern = "^[0-9]{8}$"
        for partner in self:
            if re.match(pattern, partner.dni):
                return True
            else:
                raise exceptions.ValidationError(_("Invalid DNI."))

    civil_status = fields.Selection(
        [
            ("single", "Single"),
            ("married", "Married"),
            ("divorced", "Divorced"),
        ]
    )

    birthdate = fields.Date()

    dni = fields.Char(string="DNI")
