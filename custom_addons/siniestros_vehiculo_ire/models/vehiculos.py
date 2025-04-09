from odoo import models, fields

class HerenciaVehiculo (models.Model):
    _inherit='mi_modulo.vehiculo'

    siniestros=fields.One2many('historial_de_siniestros','cliente', string='Siniestros')




