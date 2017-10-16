# -*- coding: utf-8 -*-
# Copyright 2017 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Payment Ogone 3D-Secure',
    'version': '10.0.1.0.0',
    'category': 'Custom',
    'summary': 'Allows to activate the 3D Secure payments using Ogone',
    'author': 'Sylvain Garancher',
    'website': 'http://www.Syleam.fr/',
    'depends': [
        'payment_ogone',
    ],
    'data': [
        'views/template.xml',
        'views/payment_acquirer.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
