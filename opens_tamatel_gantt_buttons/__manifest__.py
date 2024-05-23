{
    'name': "Botones en Gantt - Tamatel",
    'summary': "3 botones en gantt para el cliente Tamatel",

    'description': """ 3 botones en gantt para el cliente Tamatel
    """,
    'author': "Open Solutions",
    'website': "https://www.opens.cl",
    'version': '1.0.1',
    'depends': ['project_enterprise', 'web_gantt'],
    # always loaded
    'data': [
        'data/ir_config_parameter.xml',
        'views/project_views.xml'
    ],

    'assets': {
        'web.assets_backend': [
            'opens_tamatel_gantt_buttons/static/src/views/*',
        ],
    },

    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
