{
    'name': 'Admin Task Audit',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Auditoría y puntaje de tareas para administradores',
    'depends': ['project'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_audit_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}