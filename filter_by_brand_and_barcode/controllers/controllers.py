# -*- coding: utf-8 -*-
# from odoo import http


# class FilterByBrandAndBarcode(http.Controller):
#     @http.route('/filter_by_brand_and_barcode/filter_by_brand_and_barcode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filter_by_brand_and_barcode/filter_by_brand_and_barcode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filter_by_brand_and_barcode.listing', {
#             'root': '/filter_by_brand_and_barcode/filter_by_brand_and_barcode',
#             'objects': http.request.env['filter_by_brand_and_barcode.filter_by_brand_and_barcode'].search([]),
#         })

#     @http.route('/filter_by_brand_and_barcode/filter_by_brand_and_barcode/objects/<model("filter_by_brand_and_barcode.filter_by_brand_and_barcode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filter_by_brand_and_barcode.object', {
#             'object': obj
#         })
