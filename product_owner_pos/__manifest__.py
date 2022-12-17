{
    'name': "Product Owner",
    'version': '15.0.1.0.0',
    'depends': ['base', 'point_of_sale', 'product', 'contacts'],
    'category': 'Category',
    'application': False,
    'description': "Product owner field in pos",

    'data': [
        'views/product_owner.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/product_owner_pos/static/src/js/owner_field_product.js',
            '/product_owner_pos/static/src/js/owner_field_receipt.js'
        ],
        'web.assets_qweb': [
            '/product_owner_pos/static/src/xml/owner_field_product.xml',
            '/product_owner_pos/static/src/xml/owner_field_receipt.xml',
        ],
    },
}
