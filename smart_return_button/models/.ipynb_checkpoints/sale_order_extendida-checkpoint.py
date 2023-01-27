# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderExtendida(models.Model):
    _inherit = "sale.order"
    
    picking_returns = fields.One2many('stock.picking', 'sale_id', string='Devoluciones')
    
    #One2many(related='picking_ids', string='Devoluciones', compute='_get_returns_ids')
    returns_count = fields.Integer(string='Cantidad de Devoluciones', compute='_compute_returns')
    
    
    @api.depends('picking_ids')
    def _get_returns_ids(self):
        for order in self:
            for pick in order.picking_ids:
                if (pick.picking_type_code == 'incoming' and pick.location_id.usage == 'customer') or\
                   (pick.picking_type_code == 'outgoing' and pick.state == 'done'):
                    order.picking_returns = (4, pick)
                          
    

    @api.depends('picking_returns')
    def _compute_returns(self):
        for order in self:
            order.returns_count = len(order.picking_returns)
            
    def _get_action_view_returns(self, pickings):

        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_picking_tree_all")

        if len(pickings) > 1:
            action['domain'] = [('id', 'in', pickings.ids)]
        elif pickings:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pickings.id

        action['context'] = dict(self._context, default_partner_id=self.partner_id.id,
                                 default_picking_type_id=pickings.picking_type_id.id, 
                                 default_origin=self.name, default_group_id=pickings.group_id.id)
        return action            
            
            
            
    def action_view_return(self):
        return self._get_action_view_returns(self.picking_returns)
