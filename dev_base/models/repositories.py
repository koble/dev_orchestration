# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _
from urlparse   import urlparse
import validators

class repositories(models.Model):
     _name = 'dev_orchestration.repositories'
     _description = 'Development Repositories'
     _sql_constraints = [
                          ('repository_unique',
                           'UNIQUE(name)',
                           'This Repository already exists !'),
                        ]

     name = fields.Char(compute="_strip_name", store=True)
     repository   = fields.Char(
         help='A full repository address\n' +
              'ex: http://github.com/koble/ocb',
         placeholder='https://github.com/<organization>/<repository>',
     )
     description  = fields.Text()
     branches_ids = fields.Many2many('dev_orchestration.branches', 
         string='Branches',
         ondelete='cascade',
         auto_join=True,
     )


     @api.depends('repository')
     def _strip_name(self):
         try:
             if validators.url(self.repository):
                 o = urlparse(self.repository)
                 self.name = o.path[1:]
         except:
             pass

     @api.constrains('repository')
     def _validate_url(self):
         if not validators.url(self.repository):
             raise exceptions.except_orm(
                 _('Invalid Repository'),
                 _('This is not a valid repository url!') +
                 _('\nPlease correct and try again.'))
