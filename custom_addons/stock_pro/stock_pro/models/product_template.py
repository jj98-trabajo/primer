
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    precio_costo = fields.Float(string='Precio de costo')
    porcentaje_ganancia = fields.Float(string='Porcentaje de ganancia (%)')
    stock_minimo = fields.Float(string='Stock mínimo')
    alerta_stock = fields.Boolean(string='Stock bajo', compute='_compute_alerta_stock')
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento')
    activo = fields.Boolean(string='Activo', default=True)

    @api.depends('qty_available', 'stock_minimo')
    def _compute_alerta_stock(self):
        for record in self:
            record.alerta_stock = record.qty_available < record.stock_minimo

    @api.onchange('precio_costo', 'porcentaje_ganancia')
    def _calcular_precio_venta(self):
        for record in self:
            if record.precio_costo and record.porcentaje_ganancia:
                record.list_price = record.precio_costo * (1 + (record.porcentaje_ganancia / 100))
