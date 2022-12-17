{
    'name': "Crm Commission",
    'version': '15.0.1.0.0',
    'depends': ['base', 'crm', 'sale_management'],
    'category': 'Category',
    'application': True,
    'description': "Crm Commission",
    'data': [
        'security/ir.model.access.csv',
        'views/crm_commission.xml',
        'views/sales_team_view.xml',
        'views/sale_person_view.xml',
        'views/total_commission.xml',
        'views/team_member_view.xml',

    ],

}
