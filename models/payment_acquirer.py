# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    ogone_force_3ds = fields.Boolean(
        string='Force 3DS',
        help='Check this box to force the 3DS activation on all payments.')
    ogone_3ds_minimum_amount = fields.Float(
        string='3DS Minimum Amount',
        help='Minimum amount needed to activate the 3D Secure on a payment.\n'
        '0 = No 3DS activation depending on the amount.'
    )

    def _check_activate_3ds(self, values):
        # The amount is sometimes passed upper or lower case
        amount = values.get('amount', 0)
        if 'AMOUNT' in values:
            amount = float(values['AMOUNT']) / 100

        return 'enable_3dsecure' in self.env.context or \
            self.ogone_force_3ds or \
            (0 < self.ogone_3ds_minimum_amount <= amount)

    def _ogone_generate_shasign(self, inout, values):
        if self._check_activate_3ds(values):
            values['FLAG3D'] = 'Y'

        return super(PaymentAcquirer, self)._ogone_generate_shasign(
            inout, values)

    def ogone_form_generate_values(self, values):
        if self._check_activate_3ds(values):
            values['FLAG3D'] = 'Y'

        return super(PaymentAcquirer, self).ogone_form_generate_values(
            values)
