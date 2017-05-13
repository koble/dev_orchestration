# -*- coding: utf-8 -*-
{
    'name': "Odoo Development Orchestration",

    'summary': """
        Adds the capacity to control your Development work.
        """,

    'description': """
        It adds the following features:
        - Repository Control
        - Branches Control by mapping the development roadmap.
        - Commits Control by identifying which commits are integrated to each 
          branch.
        - Upstream compare, shows the commit differences between your branch
          and the upstream, helping to identify missing commits for better
          code stability.
        - Dashboard to allow control in only one place.
        - And more to come...
        """,

    'author': "Koble Open Solutions",
    'website': "http://www.koble.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',
#    'license': 'LGPL',
    'website': 'https://github.com/koble/orchestrator',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/orchestration.xml',
        'views/repositories.xml',
        'views/branches.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
