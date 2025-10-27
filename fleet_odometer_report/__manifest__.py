# -*- coding: utf-8 -*-
{
    "name": "Fleet Odometer Report",
    "summary": "Reporte de odómetro por vehículo o conductor con filtros por fecha",
    "version": "18.0.1.0.0",
    "author": "Paulo-Hernandez","Tamatel SPA"
    "license": "LGPL-3",
    "depends": ["fleet"],
    "data": [
        "security/ir.model.access.csv",
        "views/fleet_odometer_report_views.xml",
        "views/fleet_odometer_report_menu.xml",
        
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}