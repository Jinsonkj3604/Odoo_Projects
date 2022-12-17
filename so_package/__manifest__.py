{
    'name': "sale package",
    'version': '15.0.1.0.0',
    'depends': ['base', 'stock', 'sale_management', 'contacts'],
    'category': 'Category',
    'application': True,
    'description': "Sale Package",


    'assets': {
        'web.assets_backend': [
            'so_package/static/src/js/action_manager.js'],
        },

    'data': [
        'security/ir.model.access.csv',
        'report/package_report_pdf.xml',
        'report/pdf_template.xml',
        'views/sale_pack_inherit.xml',
        'views/sale_pack_notebook.xml',
        'views/sale_package_bundle.xml',
        'views/pack_bundle_view.xml',
        'views/package_bundle_button.xml',
        'views/sale_package.xml',
        'wizards/pdf_report.xml',
    ],

               }
