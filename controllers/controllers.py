# -*- coding: utf-8 -*-
# from odoo import http


# class PreConfigureVoip(http.Controller):
#     @http.route('/pre_configure_voip/pre_configure_voip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pre_configure_voip/pre_configure_voip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pre_configure_voip.listing', {
#             'root': '/pre_configure_voip/pre_configure_voip',
#             'objects': http.request.env['pre_configure_voip.pre_configure_voip'].search([]),
#         })

#     @http.route('/pre_configure_voip/pre_configure_voip/objects/<model("pre_configure_voip.pre_configure_voip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pre_configure_voip.object', {
#             'object': obj
#         })
