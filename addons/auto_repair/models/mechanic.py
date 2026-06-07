# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Mechanic(models.Model):
    _name = 'auto_repair.mechanic'
    _description = 'Mechanic'

    name = fields.Char(required=True)