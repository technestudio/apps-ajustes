from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = "sale.report"

    marca = fields.Char("Marca", readonly=True)
    barcode = fields.Char("Código de barra", readonly=True)
    default_code = fields.Char("Referencia interna", readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['marca'] = ", t.x_studio_marca AS marca"
        fields['barcode'] = ", p.barcode as barcode"
        fields['default_code'] = ", p.default_code"
        groupby += ", t.x_studio_marca, p.barcode, p.default_code"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
