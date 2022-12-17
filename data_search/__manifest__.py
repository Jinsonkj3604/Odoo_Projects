{
    'name': "Data Search",
    'version': '15.0.1.0.0',
    'depends': ['base', 'mail'],
    'category': 'Category',
    'application': True,
    'description': "Data search in all models",
    'data': [
        'security/ir.model.access.csv',
        'views/data_search_field.xml',
        'views/data_search_page.xml'
    ],

}
