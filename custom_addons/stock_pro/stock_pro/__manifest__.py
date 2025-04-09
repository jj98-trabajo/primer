{
    'name': 'Inventario PRO',
    'version': '1.0',
    'author': 'Tu Nombre',
    'category': 'Inventory',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
}
