{
    'name': "website maintenance request",
    'version': '15.0.1.0.0',
    'depends': ['base', 'website', 'mrp', 'maintenance', 'mail', 'contacts'],
    'category': 'Category',
    'application': True,
    'description': "Website Maintenance Request",

    'data': [
        'data/mail_template.xml',
        'views/maintenance_page.xml',
        'views/maintenance_form.xml',
        'views/maintenance_thanks.xml'

    ],
}
