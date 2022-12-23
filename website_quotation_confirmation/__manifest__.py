{
    'name': "Website Quotation Confirmation",
    'version': "15.0.1.0.0",
    'depends': ['base', 'website','website_sale'],
    'category': 'Category',
    'application': True,
    'description': 'customer website quotation confirmation',

    'data': [
        'views/confirm_button.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/website_quotation_confirmation/static/src/js/check_button.js',
        ],

    },
}