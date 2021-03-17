# -*- coding: utf-8 -*-
# from odoo import http


# class Da(http.Controller):
#     @http.route('/da/da/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/da/da/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('da.listing', {
#             'root': '/da/da',
#             'objects': http.request.env['da.da'].search([]),
#         })

#     @http.route('/da/da/objects/<model("da.da"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('da.object', {
#             'object': obj
#         })
