from odoo import models, fields

class editorial(models.Model):
    _name = 'library.editorial'
    _description = 'Editorial'

    name = fields.Char("Editorial", size=64, required=True)
    book_ids = fields.One2many('library.book', 'editorial_id', string="Libros")
