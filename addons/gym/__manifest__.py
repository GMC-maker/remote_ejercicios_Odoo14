{
    'name': "gym",
    'summary': """Gestion del modulo Gym""",
    'description': """Gestion de clases, usuarios, material, etc""",
    'author': "TSI - UPO",
    'author': "http://www.upo.es",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/classes_views.xml',
        'views/menu_views.xml'
    ],
    'demo': [
    'demo/demo.xml',
    ],
    'application': True,
}