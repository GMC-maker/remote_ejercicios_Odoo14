# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RepairOrder(models.Model):
    _name = 'auto_repair.repair_order'
    _description = 'Repair Order'

    name = fields.Char(required=True)