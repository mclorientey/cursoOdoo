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
    'version': '14.0.1.0.0',
    'installable': True,
    'application': True,
    'depends': ['base',
                ],
    
    # always loaded
    'data': [   
        'views/library_actions.xml',                 
    ],
    'qweb': [
        
    ],
    # only loaded in demonstration mode
}
