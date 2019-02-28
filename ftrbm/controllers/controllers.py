# -*- coding: utf-8 -*-
from odoo import http

# class Ftrbm(http.Controller):
#     @http.route('/ftrbm/ftrbm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ftrbm/ftrbm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ftrbm.listing', {
#             'root': '/ftrbm/ftrbm',
#             'objects': http.request.env['ftrbm.ftrbm'].search([]),
#         })

#     @http.route('/ftrbm/ftrbm/objects/<model("ftrbm.ftrbm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ftrbm.object', {
#             'object': obj
#         })