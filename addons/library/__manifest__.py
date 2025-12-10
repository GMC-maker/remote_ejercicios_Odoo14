{
    'name': "library",
    'version': '1.0',
    'author': "Tu Nombre",
    'website': "http://www.example.com",
    'category': 'Education',
    'summary': "Gestión de libros, autores y editoriales",
    'description': """
Aplicación Library: permite gestionar libros, autores y editoriales.
    """,

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/author_view.xml',
        'views/editorial_view.xml',
        'views/menu_view.xml',
    ],

    'application': True,
}
