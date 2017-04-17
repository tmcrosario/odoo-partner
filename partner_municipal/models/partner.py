# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    merchant = fields.Boolean()

    drei_ids = fields.One2many(
        comodel_name='municipal.drei',
        inverse_name='partner_id'
    )
