# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    ogone_force_3ds = fields.Boolean(
        string='Force 3DS',
        help='Check this box to force the 3DS activation on all payments.')

    def _ogone_generate_shasign(self, inout, values):
        if 'enable_3dsecure' in self.env.context or self.ogone_force_3ds:
            values['FLAG3D'] = 'Y'

        return super(PaymentAcquirer, self)._ogone_generate_shasign(
            inout, values)

    def ogone_form_generate_values(self, values):
        if 'enable_3dsecure' in self.env.context or self.ogone_force_3ds:
            values['FLAG3D'] = 'Y'

        return super(PaymentAcquirer, self).ogone_form_generate_values(
            values)
