{
    'name': "Import Lot and Serial",
    'version': '15.0.1.0.0',
    'depends': ['base', 'stock'],
    'category': 'Category',
    'application': True,
    'description': "Import Lot and Serial number",
    'data': [
        'security/ir.model.access.csv',
        'wizard/lot_serial_number.xml',
        'views/import_view.xml'
        ],

}
