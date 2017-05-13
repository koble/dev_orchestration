# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class branches(models.Model):
     _name = 'dev_orchestration.branches'
     _Description = 'Development Branches'

     name        = fields.Char()
     branch_type = fields.Selection(
       [('Prod','Production'),('UAT','User Acceptance Test'),('Dev','Development')],
       'Type',
     )
     description = fields.Text()
     repositories_ids = fields.Many2many('dev_orchestration.repositories',
       string="Repositories",
     )
