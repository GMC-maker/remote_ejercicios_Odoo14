from odoo import models, fields, api

class author(models.Model):
    _name = 'library.author'
    _description = 'Autor'

    name = fields.Char("Nombre", size=64, required=True)
    nationality = fields.Many2one("res.country", string="Nacionalidad")
    birthday = fields.Date("Fecha de nacimiento")

    libros_ids = fields.Many2many('library.book', string="Libros")
