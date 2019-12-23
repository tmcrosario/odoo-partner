from odoo import models, fields


class Partner(models.Model):

    _name = 'res.partner'
    _inherit = 'res.partner'

    civil_status = fields.Selection([('single', 'Single'),
                                     ('married', 'Married'),
                                     ('divorced', 'Divorced')])

    birthdate = fields.Date()
