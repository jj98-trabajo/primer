# -*- coding: utf-8 -*-
# from odoo import http


# class InventarioGanancia(http.Controller):
#     @http.route('/inventario_ganancia/inventario_ganancia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario_ganancia/inventario_ganancia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario_ganancia.listing', {
#             'root': '/inventario_ganancia/inventario_ganancia',
#             'objects': http.request.env['inventario_ganancia.inventario_ganancia'].search([]),
#         })

#     @http.route('/inventario_ganancia/inventario_ganancia/objects/<model("inventario_ganancia.inventario_ganancia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario_ganancia.object', {
#             'object': obj
#         })

