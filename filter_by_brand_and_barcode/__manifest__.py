# -*- coding: utf-8 -*-
{
    
    'name': "Filtros en informes Tablero y Ventas",    
    
    'shortdesc': "Nuevos filtros en informes de Venta.",

    'summary': """
        Incluye un filtro por Marca, 
        Código de barra y Referencia interna
        en las vistas Tablero y Ventas.
    """,

    'description': """
        Filtro por marca, código de barra y referencia interna 
        en informes Tablero y Ventas del módulo Ventas
    """,    
    
    'description_html': """
    <span>
        Incluye un filtro por: Marca, Código de barra y Referencia Interna 
        en las vistas: Tablero y Ventas, de la opción de Informes del módulo
        de Ventas. Agrega el campo Marca en la ficha del producto.
    </span>
    """,
    
    'author': "Techne Studio IT & Consulting",
    'website': "https://technestudioit.com/",

    'license': "Other proprietary",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',    
    'installed_version': '15.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
