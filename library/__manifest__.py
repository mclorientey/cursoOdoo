# -*- coding: utf-8 -*-
{
    'name': 'Biblioteca',

    'summary': 'Biblioteca Virtual',

    'description': 'Módulo de una biblioteca virtual para ir cogiendo los conceptos de Odoo paso a paso',

    'author': 'Curso Odoo',
    'contributors': [
                     "Carmen Loriente <carmen.loriente@altia.es>"
                     ],
    'website': "http://www.altia.es",
    'category': 'Altia Desarrollo',
    'version': '14.0.2.0.0',
    'installable': True,
    'application': True,
    'depends': ['base','mail', 'hr', 'product'
                ],
    
    # always loaded
    'data': [  
        
        'views/library_book_view.xml',                         
        'views/library_booking_view.xml',
        'views/library_category_book_view.xml',
        'views/library_review_view.xml',
        'views/product_template_view.xml',
        'report/library_booking_report.xml',
        'report/library_book_report.xml',
        'wizard/library_booking_wizard.xml',
        'wizard/library_booking_report_wizard.xml',
        'security/ir.model.access.csv', 
        'views/library_actions.xml',
        'views/library_menus.xml',

    ],
    'qweb': [
        
    ],
    # only loaded in demonstration mode
}
