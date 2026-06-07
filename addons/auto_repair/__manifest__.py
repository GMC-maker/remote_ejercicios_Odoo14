# -*- coding: utf-8 -*-
{
    'name': "auto_repair",

    'summary': """
        practia de examen ODOO de enero 2026""",

    'description': """
        Gestion de Reparaciones en un taller.
    """,

    'author': "Gabriela Celano",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Logistics',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mechanic_views.xml',
        'views/repair_order_views.xml',
        'views/menu.xml',
    ],
    
    'application': True,
    'installable': True,
}
