# -*- coding: utf-8 -*-
# from odoo import http


# class Estate2(http.Controller):
#     @http.route('/estate2/estate2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate2/estate2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate2.listing', {
#             'root': '/estate2/estate2',
#             'objects': http.request.env['estate2.estate2'].search([]),
#         })

#     @http.route('/estate2/estate2/objects/<model("estate2.estate2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate2.object', {
#             'object': obj
#         })
