# -*- coding: utf-8 -*-
{
    'name': "FTRBM",

    'summary': """
        Federación territorial riojana de balonmano.""",

    'description': """
        Gestión de partidos, equipos y personal de la Federación Terriorial Riojana de Balonmanoself.
        Puedes gestionar desde los mesas y árbitros hasta los jugadores y entenadores de los equipos.
    """,

    'author': "Erik Garcia Dominguez",
    'website': "https://www.ftrbm.org/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestor',
    'version': '1.16',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
