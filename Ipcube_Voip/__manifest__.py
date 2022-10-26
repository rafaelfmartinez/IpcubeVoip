# -*- coding: utf-8 -*-
{
    'name': "IPCUBE_VOIP",

    'summary': "Integration of VOIP with IPCUBE",

    'description': "Ipcube provides voip connectivity to businesses. Our IPCUBE app simplifies connection of your Odoo implementation to the local and international telephony network. You may use Ipcube connector to integrate your existing voice provider or using the Ipcube network.  Now your Odoo users will be able to make and receive phone calls in their browsers from other users or from any phone and to any phone.  This module is free to install, but you must contact ipcube.net to activate service.",

    'author': "IPCUBE",
    'website': "https://ipcube.net",
    'license': "LGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','voip',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
