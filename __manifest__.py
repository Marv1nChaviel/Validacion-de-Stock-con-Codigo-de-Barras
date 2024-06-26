{
    'name': 'Validacion con Codigo de Barras',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Validate products in pickings using barcode scanner',
    'description': 'This module allows inventory staff to validate products in pickings by scanning barcodes.',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
}
