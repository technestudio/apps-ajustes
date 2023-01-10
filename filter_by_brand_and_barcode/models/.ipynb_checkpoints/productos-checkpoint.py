# -*- coding: utf-8 -*-

from odoo import models, api, fields

class ProductosExtendidos(models.Model):
    
    _inherit = 'product.template'
    _description = 'Extensión a la ficha del Producto'
    
    x_studio_marca = fields.Char(string='Marca')
    