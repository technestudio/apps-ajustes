# -*- coding: utf-8 -*-
{
    
    'name': "free_port_branch",   

    'summary': """
        Manejo especial de impuestos para sucursales de tipo puerto libre.
    """,

    'description': """
        Incluye un cambio automático en la generación de los presupuestos, 
        en el que sí, es un pedido de una sucursal configurada como puerto libre,
        el impuesto de la línea de pedido es Exento (a pesar de la configuración que tenga el producto).
    """,    
    
    'author': "Techne Studio IT & Consulting",
    'website': "https://technestudioit.com/",

    'license': "Other proprietary",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',    
    'installed_version': '15.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
