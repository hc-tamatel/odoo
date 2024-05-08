from odoo import models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def custom_group_1(self):
        """
        This method will be called from button that we have created using owl js
        """
        field = self.env['ir.config_parameter'].get_param('gantt_group_by_button_field_1', 'project_id')
        return {
            'name': 'Tareas',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'gantt',
                    'res_model': 'project.task',
                    'target': 'current',
                    'views': [(self.env.ref('project_enterprise.project_task_view_gantt').id, 'gantt')],
                    'context': {'search_default_open_tasks': 1,
                                'default_scale':'week',
                                'group_by': field}
        }

    @api.model
    def custom_group_2(self):
        """
        This method will be called from button that we have created using owl js
        """
        field = self.env['ir.config_parameter'].get_param('gantt_group_by_button_field_2', 'user_ids')
        return {
            'name': 'Tareas',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'gantt',
                    'res_model': 'project.task',
                    'target': 'current',
                    'views': [(self.env.ref('project_enterprise.project_task_view_gantt').id, 'gantt')],
                    'context': {'search_default_open_tasks': 1,
                                'default_scale': 'week',
                                'group_by': field}
        }

    @api.model
    def custom_group_3(self):
        """
        This method will be called from button that we have created using owl js
        """
        field_1 = self.env['ir.config_parameter'].get_param('gantt_group_by_button_field_2', 'project_id')
        field_2 = self.env['ir.config_parameter'].get_param('gantt_group_by_button_field_1', 'user_ids')
        return {
            'name': 'Tareas',
            'type': 'ir.actions.act_window',
            'view_mode': 'gantt',
            'res_model': 'project.task',
            'target': 'current',
            'views': [(self.env.ref('project_enterprise.project_task_view_gantt').id, 'gantt')],
            'context': {'search_default_open_tasks': 1,
                        'default_scale': 'week',
                        'group_by': [field_1, field_2]}
        }
