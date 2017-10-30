# -*- coding: utf-8 -*-
# Copyright 2017 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestOgone3Ds(common.TransactionCase):
    def setUp(self):
        super(TestOgone3Ds, self).setUp()

        self.acquirer = self.env.ref('payment.payment_acquirer_ogone')

    def test_render_without_3ds(self):
        """ Test to render the form without 3ds """
        html = self.acquirer.render(None, 164.23, None)
        self.assertIn(
            '<input type="hidden" name="FLAG3D"/>', html)
        self.assertNotIn(
            '<input type="hidden" name="FLAG3D" value="Y"/>', html)

    def test_render_with_3ds(self):
        """ Test to render the form with 3ds on the fly """
        html = self.acquirer.with_context(enable_3dsecure=True).render(
            None, 164.23, None)
        self.assertIn(
            '<input type="hidden" name="FLAG3D" value="Y"/>', html)
        self.assertNotIn(
            '<input type="hidden" name="FLAG3D"/>', html)

    def test_render_forced_3ds(self):
        """ Test to render the form with forced 3ds """
        self.acquirer.ogone_force_3ds = True
        html = self.acquirer.render(None, 164.23, None)
        self.assertIn(
            '<input type="hidden" name="FLAG3D" value="Y"/>', html)
        self.assertNotIn(
            '<input type="hidden" name="FLAG3D"/>', html)

    def test_minimum_amount_not_reached(self):
        """ Test to render the form when the minimum amount is not reached """
        self.acquirer.ogone_3ds_minimum_amount = 250
        html = self.acquirer.render(None, 164.23, None)
        self.assertIn(
            '<input type="hidden" name="FLAG3D"/>', html)
        self.assertNotIn(
            '<input type="hidden" name="FLAG3D" value="Y"/>', html)

    def test_minimum_amount_reached(self):
        """ Test to render the form when the minimum amount is reached """
        self.acquirer.ogone_3ds_minimum_amount = 250
        html = self.acquirer.render(None, 813.34, None)
        self.assertIn(
            '<input type="hidden" name="FLAG3D" value="Y"/>', html)
        self.assertNotIn(
            '<input type="hidden" name="FLAG3D"/>', html)
