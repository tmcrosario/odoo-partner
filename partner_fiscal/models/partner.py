import re

from odoo import models, fields, api, _, exceptions


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    __check_cuit_re = re.compile(r'([0-9]{2}\-[0-9]{8}\-[0-9]{1})$',
                                 re.IGNORECASE)

    def _validate_cuit(self):
        if len(self.cuit) != 13 or self.cuit[2] != '-' or self.cuit[11] != '-':
            return False

        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

        cuit = self.cuit.replace('-', '')

        aux = 0
        for i in xrange(10):
            aux += int(cuit[i]) * base[i]

        aux = 11 - (aux - (int(aux / 11) * 11))

        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9

        return aux == int(cuit[10])

    @api.constrains('cuit')
    def _check_cuit(self):
        if self.cuit:
            if not self.__check_cuit_re.match(
                    self.cuit) and not self._validate_cuit():
                raise exceptions.UserError(_('Invalid CUIT'),
                                           _('Valid format: XX-XXXXXXXX-X'))

    cuit = fields.Char(string='CUIT', size=13, help='Format: XX-XXXXXXXX-X')

    fiscal_situation = fields.Selection([('monotributista', 'Monotributista'),
                                         ('responsable_inscripto',
                                          'Responsable Inscripto')])
