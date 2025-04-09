from odoo import models, fields, api

class HistorialSiniestros(models.Model):
    _name = 'historial_de_siniestros'
    _description = 'Modelo para gestionar siniestros'
    cliente=fields.Many2one('mi_modulo.vehiculo', string="Cliente/Vehículo")
    tipos=fields.Many2one('historial_de_siniestros.tipos_de_siniestros', string="Tipo")
    totaldelgasto=fields.Integer(string='Total del gasto')
    cubiertoenporcentaje=fields.Float(string='Porcentaje del gasto cubierto')
    gastoenpesos=fields.Integer(string='Total cubierto en pesos', compute='_compute_total_cubierto')
    fechadelsiniestro=fields.Date(string='Fecha del siniestro')
    descripcion=fields.Char(string='Descripción del hecho')

    @api.depends('totaldelgasto', 'cubiertoenporcentaje')
    def _compute_total_cubierto(self):
        for siniestro in self:
            siniestro.gastoenpesos = siniestro.totaldelgasto * (siniestro.cubiertoenporcentaje / 100)


class TiposSiniestros(models.Model):
    _name='historial_de_siniestros.tipos_de_siniestros'
    _description = 'Tipos de Siniestros'
    _rec_name='name'
    name= fields.Char(string='Tipos', required=True)
