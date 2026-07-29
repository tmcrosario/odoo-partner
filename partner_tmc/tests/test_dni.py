from odoo.exceptions import ValidationError

from odoo.tests import common


class TestDni(common.TransactionCase):
    def test_batch_create_valid_dni(self):
        # The constraint must iterate the recordset, not crash on a batch
        partners = self.env["res.partner"].create(
            [
                {"name": "DNI A", "dni": "12345678"},
                {"name": "DNI B", "dni": "87654321"},
            ]
        )
        self.assertEqual(len(partners), 2)

    def test_invalid_dni_rejected(self):
        with self.assertRaises(ValidationError):
            self.env["res.partner"].create({"name": "DNI C", "dni": "1234567"})

    def test_trailing_newline_rejected(self):
        # `$` matched before a newline; fullmatch must reject it
        with self.assertRaises(ValidationError):
            self.env["res.partner"].create({"name": "DNI D", "dni": "12345678\n"})
