# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class love_match_r(models.Model):
#     _name = 'love_match_r.love_match_r'
#     _description = 'love_match_r.love_match_r'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
