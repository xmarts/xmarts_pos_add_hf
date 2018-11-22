# -*- coding: utf-8 -*-
{
    'name': "POS Encabezado/Pie de pagina V2",

    'summary': "Para odoo12",

    'description': "Agrega un encabezado y un pie de pagina al ticket del POS",

    'author': "Pablo Osorio",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        'static/src/xml/assets.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/pos.xml'
    ],
}
