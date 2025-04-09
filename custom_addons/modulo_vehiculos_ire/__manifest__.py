{
    'name': 'Módulo de Vehículos',
    'version': '1.0',
    'summary': 'Gestión de vehículos',
    'author': 'Irene Colichelli',
    'website': 'Tu Sitio Web',
    'category': 'Inventory',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/vistas.xml',
        'views/partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
