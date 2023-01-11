# -*- coding: utf-8 -*-
{
    
    'name': "smart_button_internal_transfers",   

    'summary': """
        Botón inteligente de las transferencias internas realizadas sobre un producto.
    """,

    'description': """
        Incluye un botón inteligente en la ficha del producto, 
        que muestra las transferencias internas realizadas sobre 
        ese producto según la sucursal en la que se encuentre el usuario.
    """,    
    
    'author': "Techne Studio IT & Consulting",
    'website': "https://technestudioit.com/",

    'license': "Other proprietary",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
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
