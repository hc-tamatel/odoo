{
    'name': 'Ponderado Soporte Operativo',
    'version': '1.0',
    'summary': 'Evaluación de calidad con cálculo ponderado en Tareas',
    "author": "Tamatel SPA",
    'category': 'Services/Helpdesk',
    'depends': ['base', 'project', 'helpdesk'],
    'data': [
        'security/security.xml',
        'views/audit_view.xml',
        'views/report_consolidado.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}