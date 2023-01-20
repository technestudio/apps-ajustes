# -*- coding: utf-8 -*-
{
    'name': "Restricciones para: extractos bancarios, conciliaciones y rompimiento de conciliaciones",

    'summary': """
        Restringe el la visualización de información de acuerdo a la rama activa o la rama permitida de un usuario.
    """,

    'description': """
         Crea grupos de usuarios especiales para la gestion (guardar, publicar y validar) 
         de extractos bancarios, conciliacion de pagos y rompimiento de conciliaciones.
    """,

    'author': "Techne Studio IT & Consulting",
    'website': "https://technestudioit.com/",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '1.0',
    'installed_version': '15.0.2.0',

    'license': 'Other proprietary',

    # any module necessary for this one to work correctly
    'depends': ['base', 'branch'], # 'account',

    # always loaded
    'data': [
        'security/crear_e_importar_extractos_bancarios.xml',
        'views/account_bank_statement_restrictions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
