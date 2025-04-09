from odoo import models, fields, api
from datetime import timedelta

class Vehiculo(models.Model):
    _name = 'mi_modulo.vehiculo'
    _description = 'Modelo para gestionar vehículos'
    _rec_name = 'placa'
    # Atributos comunes de un vehículo
    marca = fields.Many2one('modulo_vehiculos_ire.marca_vehiculo', string='Marca')
    modelo = fields.Char(string='Modelo', required=True)
    color = fields.Char(string='Color')
    ano_fabricacion = fields.Integer(string='Año de Fabricación')
    placa = fields.Char(string='Placa')
    conductor= fields.Many2one('res.partner', string='Conductor')
    ultima_fecha_pago = fields.Date(string='Última fecha de pago')
    vencimiento_seguro = fields.Date(string='Vencimiento del Seguro', compute='_compute_vencimiento_seguro', store=False)
    productos= fields.Many2one('product.product', string='Plan')
    def _compute_vencimiento_seguro(self):
        for vehiculo in self:
            if vehiculo.ultima_fecha_pago:
                vehiculo.vencimiento_seguro = vehiculo.ultima_fecha_pago + timedelta(days=30)
            else:
                vehiculo.vencimiento_seguro = False
     #Este campo va a verificar que la marca del auto este completada para poder continuar
    @api.constrains('marca')
    def _check_marca_condition(self):
        for record in self:
            if not record.marca:
                raise ValidationError("El campo 'marca' no puede estar vacío.")

    @api.constrains('ano_fabricacion')
    def _check_ano_faricacion_constraint(self):
        for record in self:
            if record.ano_fabricacion and record.ano_fabricacion <= 1990:
                raise ValueError("El campo 'Año de fabricación' debe ser mayor a 1990.")

class MarcaVehiculo(models.Model):
    _name = 'modulo_vehiculos_ire.marca_vehiculo'
    _description = 'Marcas de Vehículos'
    _rec_name = 'name'
    name = fields.Char(string='Marca', required=True)



