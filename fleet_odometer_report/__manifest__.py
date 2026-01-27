# -*- coding: utf-8 -*-
{
    "name": "Fleet Odometer Report",
    "summary": "Reporte de odómetro por vehículo o conductor con filtros por fecha",
    "version": "1.0",
    "author": "Tamatel SPA",
    "category": "Fleet",
    "depends": ["fleet"],
    "data": [
        "security/ir.model.access.csv",
        "views/fleet_odometer_report_views.xml",
        "views/fleet_odometer_report_menu.xml",
        
    ],
    'installable': True,
    'application': False,
    "license": "LGPL-3",
}