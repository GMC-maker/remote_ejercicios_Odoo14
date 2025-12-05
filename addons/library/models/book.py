from odoo import models, fields, api

class book(models.Model):
    _name = 'library.book'
    _description = 'Libro'

    title = fields.Char("Título", size=128)
    image = fields.Binary("Imagen")
    isbn = fields.Char("ISBN", size=16)
    npage = fields.Integer("Nº de páginas")
    type = fields.Selection(
        [
            ('fantasia', 'Novela fantástica'),
            ('historia', 'Ensayo histórico'),
        ],
        string="Género"
    )

    editorial_id = fields.Many2one('library.editorial', string="Editorial")
    autores_ids = fields.Many2many('library.author', string="Autores")
