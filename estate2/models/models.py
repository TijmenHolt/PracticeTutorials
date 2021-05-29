# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estate2(models.Model):
     _name = 'estate2.estate2'
     _description = 'estate2.estate2'

     name = fields.Char()
     description = fields.Text()
     postcode = fields.Char()
     date_availability = fields.Date()
     expected_price = fields.Float()
     selling_price = fields.Floet()
     bedrooms = fields.Integer()
     living_area = fields.Integer()
     facades = fields.Integer()
     garage = fields.Boolean()
     garden = fields.Boolean()
     garden_area = fields.Integer()
     garden_orientation = fields.Selection(
         string='Garden Orientation',
         selection=[('north', 'North'), ('east', 'East'), ('west', 'West'), ('south', 'South')],
         help="Orientation is to indicate the garden orientation against the sun.")
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
