from odoo import models, fields

class MacroProject(models.Model):
    _name = 'tm.macro.project'
    _description = 'Macro Proyecto Tamatel'

    name = fields.Char(string='Nombre', required=True)

class Project(models.Model):
    _name = 'tm.project'
    _description = 'Proyecto Tamatel'

    name = fields.Char(string='Nombre', required=True)
    macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')

class SubProject(models.Model):
    _name = 'tm.subproject'
    _description = 'Sub-Proyecto Tamatel'

    name = fields.Char(string='Nombre', required=True)
    project_id = fields.Many2one('tm.project', string='Proyecto Padre')

class Site(models.Model):
    _name = 'tm.site'
    _description = 'Sitio de la Actividad'
    _rec_name = 'name'
    name = fields.Char(string='Nombre del Sitio', required=True)
    code = fields.Char(string='Código del Sitio')