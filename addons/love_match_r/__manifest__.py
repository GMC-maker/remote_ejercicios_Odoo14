# -*- coding: utf-8 -*-
{
    'name': "love_matchR",

    'summary': """
        REPASO de EXAMEN ODOO2026""",

    'description': """
        Practicar la construccion de un modulo de odoo de citas
    """,

    'author': "Gabriela Celano",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Comercial',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_views.xml',
        'views/user_views.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "application": True,
}