# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestDevOrchestration(TransactionCase):

    def test_create(self):
        "Create a simple Repository"
        Repository = self.env['dev_orchestration.repositories']
        url = Repository.create({'repository': 'https://github.com/koble/orchestration'})
        self.assertEqual(url.name, 'koble/orchestration')
