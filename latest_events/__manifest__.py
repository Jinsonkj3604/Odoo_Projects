{
    'name': "latest events",
    'version': '15.0.1.0.0',
    'depends': ['base', 'website', 'website_event'],
    'category': 'Category',
    'application': True,
    'description': "latest events snippet",

    'data': [
        'views/dynamic_snippet.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/latest_events/static/src/js/dynamic.js',
        ],
    },
}
