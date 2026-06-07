# -*- coding: utf-8 -*-
# from odoo import http


# class AutoRepair(http.Controller):
#     @http.route('/auto_repair/auto_repair/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auto_repair/auto_repair/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auto_repair.listing', {
#             'root': '/auto_repair/auto_repair',
#             'objects': http.request.env['auto_repair.auto_repair'].search([]),
#         })

#     @http.route('/auto_repair/auto_repair/objects/<model("auto_repair.auto_repair"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auto_repair.object', {
#             'object': obj
#         })
