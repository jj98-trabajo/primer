from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    precio_costo = fields.Float(string="Precio de Costo", required=True)
    porcentaje_ganancia = fields.Float(string="Ganancia (%)", required=True, default=0.0)
    precio_venta_calculado = fields.Float(string="Precio de Venta Calculado", compute="_calcular_precio_venta", store=True)

    @api.depends('precio_costo', 'porcentaje_ganancia')
    def _calcular_precio_venta(self):
        for producto in self:
            producto.precio_venta_calculado = producto.precio_costo * (1 + (producto.porcentaje_ganancia / 100))
