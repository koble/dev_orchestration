# -*- coding: utf-8 -*-
from odoo import http

# class Github-odoo(http.Controller):
#     @http.route('/github-odoo/github-odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/github-odoo/github-odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('github-odoo.listing', {
#             'root': '/github-odoo/github-odoo',
#             'objects': http.request.env['github-odoo.github-odoo'].search([]),
#         })

#     @http.route('/github-odoo/github-odoo/objects/<model("github-odoo.github-odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('github-odoo.object', {
#             'object': obj
#         })