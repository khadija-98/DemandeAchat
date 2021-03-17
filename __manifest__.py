# -*- coding: utf-8 -*-
{
    'name': "Demande Achat",
    'sequence' : 2,
    'author': 'Khadija El Kadiri',
    'website': "http://www.leansoft.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','hr'],

    'summary': """ Ce module permet au magasinier de lancer une demande achat """,

    'description':""" Ce module permet au magasinier de lancer une demande achat """,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/demande_views.xml',
        'views/templates.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
