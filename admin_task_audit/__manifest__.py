{
    'name': 'Admin Task Audit',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Auditoría y puntaje de tareas para administradores',
    'depends': ['project'],
    "author": "Tamatel SPA",
    'data': [
        'security/ir.model.access.csv',
        'views/task_audit_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'admin_task_audit/static/src/xml/audit_timer.xml',
            'admin_task_audit/static/src/js/audit_timer.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}