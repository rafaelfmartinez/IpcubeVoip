# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pre_configure_voip(models.Model):
#     _name = 'pre_configure_voip.pre_configure_voip'
#     _description = 'pre_configure_voip.pre_configure_voip'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
