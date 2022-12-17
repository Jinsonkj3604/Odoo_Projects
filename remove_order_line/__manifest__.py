{
    'name': "Remove Order Line",
    'version': '15.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'category': 'Category',
    'application': False,
    'description': "removing order lines from pos orders",

    'data': [
        'views/remove_order_line.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/remove_order_line/static/src/js/clear_all_button.js',
            '/remove_order_line/static/src/js/clear_line_button.js'
        ],
        'web.assets_qweb': [
            '/remove_order_line/static/src/xml/clear_all_button_view.xml',
            '/remove_order_line/static/src/xml/clear_line_button_view.xml',
        ],
    },
}
