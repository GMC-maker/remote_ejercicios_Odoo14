# -*- coding: utf-8 -*-
# from odoo import http


# class LoveMatchR(http.Controller):
#     @http.route('/love_match_r/love_match_r/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/love_match_r/love_match_r/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('love_match_r.listing', {
#             'root': '/love_match_r/love_match_r',
#             'objects': http.request.env['love_match_r.love_match_r'].search([]),
#         })

#     @http.route('/love_match_r/love_match_r/objects/<model("love_match_r.love_match_r"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('love_match_r.object', {
#             'object': obj
#         })
