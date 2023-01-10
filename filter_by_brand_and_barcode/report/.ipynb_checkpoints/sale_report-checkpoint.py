from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = "sale.report"
    
    marca = fields.Char(string="Marca", readonly=True)
    barcode = fields.Char("Código de barra", readonly=True)
    default_code = fields.Char("Referencia Interna", readonly=True)

    """ 
    #16.0
    
    def _group_by_sale(self):
        groupby = super()._group_by_sale()
        groupby += ", t.x_studio_marca, p.barcode, p.default_code"
        return groupby
    
    def _select_additional_fields(self):
        return { 
            'marca': 't.x_studio_marca',
            'barcode': 'p.barcode',
            'default_code': 'p.default_code',
        }    
        

    """
  

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['marca'] = ", t.x_studio_marca AS marca"
        fields['barcode'] = ", p.barcode as barcode"
        fields['default_code'] = ", p.default_code"
        groupby += ", t.x_studio_marca, p.barcode, p.default_code"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)    