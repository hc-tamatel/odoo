from odoo import models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def custom_group_1(self):
        """
        This method will be called from button that we have created using owl js
        """
        context = dict(self.env.context)
        group_filter = self.env['ir.config_parameter'].sudo().get_param('gantt_group_by_button_field_1', 'project')
        context.update({
            f'search_default_{group_filter}': 1,
            'default_scale': 'week', })
        return {
            'name': 'Tareas',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'gantt,kanban,tree,form,calendar,map,pivot,graph,activity',
                    'res_model': 'project.task',
                    'target': 'current',
                    'views': [(False, 'gantt'),
                              (False, 'kanban'),
                              (False, 'tree'),
                              (False, 'form'),
                              (False, 'calendar'),
                              (False, 'map'),
                              (False, 'pivot'),
                              (False, 'graph'),
                              (False, 'activity'),
                              ],
                    'context': context
        }

    @api.model
    def custom_group_2(self):
        """
        This method will be called from button that we have created using owl js
        """
        context = dict(self.env.context)
        group_filter = self.env['ir.config_parameter'].sudo().get_param('gantt_group_by_button_field_2', 'user')
        context.update({
            f'search_default_{group_filter}': 1,
            'default_scale':'week',})
        return {
            'name': 'Tareas',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'gantt,kanban,tree,form,calendar,map,pivot,graph,activity',
                    'res_model': 'project.task',
                    'target': 'current',
                    'views': [(False, 'gantt'),
                              (False, 'kanban'),
                              (False, 'tree'),
                              (False, 'form'),
                              (False, 'calendar'),
                              (False, 'map'),
                              (False, 'pivot'),
                              (False, 'graph'),
                              (False, 'activity'),

                              ],
                    'context': context
        }

    @api.model
    def custom_group_3(self):
        """
        This method will be called from button that we have created using owl js
        """
        context = dict(self.env.context)
        group_filter_1 = self.env['ir.config_parameter'].sudo().get_param('gantt_group_by_button_field_2', 'project')
        group_filter_2 = self.env['ir.config_parameter'].sudo().get_param('gantt_group_by_button_field_1', 'user')
        context.update({
            f'search_default_{group_filter_1}': 1,
            f'search_default_{group_filter_2}': 1,
            'default_scale': 'week', })
        return {
            'name': 'Tareas',
            'type': 'ir.actions.act_window',
            'view_mode': 'gantt,kanban,tree,form,calendar,map,pivot,graph,activity',
            'res_model': 'project.task',
            'target': 'current',
            'views': [(False, 'gantt'),
                              (False, 'kanban'),
                              (False, 'tree'),
                              (False, 'form'),
                              (False, 'calendar'),
                              (False, 'map'),
                              (False, 'pivot'),
                              (False, 'graph'),
                              (False, 'activity'),
                              ],
            'context': context
        }
