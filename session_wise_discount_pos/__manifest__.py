{
    'name': "Category Discount pos",
    'version': '15.0.1.0.0',
    'depends': ['base', 'point_of_sale', 'product'],
    'category': 'Category',
    'application': False,
    'description': "Pos Session Wise Discount on Category",

    'data': [
        'views/sessions_field.xml',

    ],
    'assets': {
        'web.assets_backend': [
            '/session_wise_discount_pos/static/src/js/session_discount.js',
        ],
    },
}
