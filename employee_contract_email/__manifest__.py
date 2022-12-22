{
    'name': "Employee Contract Expiry Email",
    'version': '15.0.1.0.0',
    'depends': ['base', 'mail', 'hr_contract', 'contacts'],
    'category': 'Category',
    'application': True,
    'description': "Employee Contract Expiry Email",
    'data': [
        'data/email_template.xml',
        'data/crone_job.xml',
        'views/expiry_date_field.xml',
        'views/reminder_field.xml'
    ],

}
