{
    'name': 'Tamatel: Stock por Proyectos',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Segregación de inventario por Macro, Proyecto y Subproyecto',
    'author': 'Paulo Hernández',
    'depends': ['stock', 'sale'], 
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_move_views.xml', 
        'views/stock_quant_views.xml',
    ],
    'installable': True,
    'application': False,
}