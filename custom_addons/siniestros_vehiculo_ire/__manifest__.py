{
    'name': 'Módulo de Siniestros',
    'version': '1.0',
    'summary': 'Gestión de siniestros',
    'author': 'Irene Colichelli',
    'website': 'Tu Sitio Web',
    'category': 'Inventory',
    'depends': ['modulo_vehiculos_ire'],
    'data': [
        'security/ir.model.access.csv',
        'views/siniestros.xml',
        'views/siniestrosvehiculos.xml'
    ],
    'installable': True,
    'auto_install': False,
}