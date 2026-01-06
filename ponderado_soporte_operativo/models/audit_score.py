from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    qa_complexity = fields.Selection([
        ('high', 'Alta'),
        ('medium', 'Media'),
        ('low', 'Baja')
    ], string='Complejidad', default='medium')

    qa_fmt_minor = fields.Integer(string='Formato: Menores', default=0)
    qa_fmt_major = fields.Integer(string='Formato: Mayores', default=0)
    qa_lang_minor = fields.Integer(string='Lenguaje: Menores', default=0)
    qa_lang_major = fields.Integer(string='Lenguaje: Mayores', default=0)
    qa_tech_minor = fields.Integer(string='Técnica: Menores', default=0)
    qa_tech_major = fields.Integer(string='Técnica: Mayores', default=0)

    qa_final_score = fields.Float(string='Calificación Final', compute='_compute_qa_score', store=True, group_operator=False)

    is_quoted = fields.Boolean(string="Cotizado", default=False, tracking=True)

    @api.depends('qa_complexity', 'qa_fmt_minor', 'qa_fmt_major', 
                 'qa_lang_minor', 'qa_lang_major', 'qa_tech_minor', 'qa_tech_major')
    def _compute_qa_score(self):
        for ticket in self:
            # 1. Calculamos primero cuánto suman los errores (Observaciones)
            obs_deduction = (ticket.qa_fmt_minor * 0.5) + \
                            (ticket.qa_fmt_major * 1.0) + \
                            (ticket.qa_lang_minor * 0.5) + \
                            (ticket.qa_lang_major * 1.5) + \
                            (ticket.qa_tech_minor * 1.7) + \
                            (ticket.qa_tech_major * 2.5)

            # 2. CONDICIÓN MAESTRA:
            if obs_deduction == 0:
                # Si NO hay errores (obs_deduction es 0), el puntaje es 100 perfecto.
                # Ignoramos la complejidad.
                ticket.qa_final_score = 100.0
            else:
                # Si SÍ hay errores, entonces aplicamos la penalización por complejidad + errores
                complexity_penalty = 0.0
                
                if ticket.qa_complexity == 'high':
                    complexity_penalty = 10.0
                elif ticket.qa_complexity == 'medium':
                    complexity_penalty = 15.0
                elif ticket.qa_complexity == 'low':
                    complexity_penalty = 20.0
                else:
                    complexity_penalty = 20.0 # Default

                # Cálculo: 100 - Penalización Complejidad - Penalización Errores
                final_score = 100.0 - complexity_penalty - obs_deduction
                
                ticket.qa_final_score = final_score

    # --- VALIDADOR DE NEGATIVOS (NUEVO) ---
    @api.constrains('qa_fmt_minor', 'qa_fmt_major', 
                    'qa_lang_minor', 'qa_lang_major', 
                    'qa_tech_minor', 'qa_tech_major')
    def _check_qa_positives(self):
        for ticket in self:
            if (ticket.qa_fmt_minor < 0 or ticket.qa_fmt_major < 0 or
                ticket.qa_lang_minor < 0 or ticket.qa_lang_major < 0 or
                ticket.qa_tech_minor < 0 or ticket.qa_tech_major < 0):

                raise ValidationError("No está permitido ingresar valores negativos en la Evaluación de Calidad.")