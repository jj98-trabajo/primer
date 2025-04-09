from odoo import models, fields

class ResPartner (models.Model):
    _inherit='res.partner'

    fechalicencia= fields.Date(string='Vencimiento de licencia')


