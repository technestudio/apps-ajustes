# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StockPickingExtendido(models.Model):
    _inherit = "stock.picking"
    
    sale_return_id = fields.Many2one(comodel_name="sale.order", string="Sales Order Return", store=True, readonly=False)
    
