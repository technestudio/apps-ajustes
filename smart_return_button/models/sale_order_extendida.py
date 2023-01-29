# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderExtendida(models.Model):
    _inherit = "sale.order"

    returns_count = fields.Integer(string='Cantidad de Devoluciones', default=0)
    
    def _get_returns_ids(self):
        return self.env['sale.order'].search(['|', 
                                              '&', 
                                              ('picking_ids.picking_type_code','=','incoming'), 
                                              ('picking_ids.location_id.usage','=','customer'),
                                              '&', 
                                              ('picking_ids.picking_type_code','=','outgoing'), 
                                              ('picking_ids.state','=','done')
                                             ])        

    
    @api.onchange('picking_ids')
    def _compute_returns(self):
        returns_ids = self._get_returns_ids()
        for order in self:
            for r_ids in returns_ids:
                if r_ids.id == order.id:
                    order.returns_count = 5

            
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
        return self._get_action_view_returns(self._get_returns_ids())
