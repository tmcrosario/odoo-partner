from odoo.exceptions import UserError

from odoo.tests import common


class TestCuit(common.TransactionCase):
    def test_batch_create_valid_cuit(self):
        # The constraint must iterate the recordset, not crash on a batch
        partners = self.env["res.partner"].create(
            [
                {"name": "Fiscal A", "cuit": "20-12345678-6"},
                {"name": "Fiscal B", "cuit": "27-23456789-1"},
            ]
        )
        self.assertEqual(len(partners), 2)

    def test_invalid_cuit_still_rejected(self):
        # Right format, wrong check digit (should be 6)
        with self.assertRaises(UserError):
            self.env["res.partner"].create(
                {"name": "Fiscal C", "cuit": "20-12345678-9"}
            )
