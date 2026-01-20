# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

# ==============================================================================
# DEFINICIÓN DE PREGUNTAS POR HITO Y POR ÁREA (IMP / IDR)
# ==============================================================================
# IMPORTANTE: Debes editar las listas dentro de 'IMP' e 'IDR' para dejar 
# solo las preguntas que correspondan a cada área.
AUDIT_QUESTIONS = {
    'H0 - TSS': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Proyecciones para la Habilitación de nuevos espacios (Power off y/o Desinstalación)",
            "Confirmación de Slots para la inserción de Tarjetas en Subrack Existentes",
            "Proyección de Espacios Nuevo Rack para Equipos (con nuevos Subracks)",
            "Proyección de Espacios Nuevo Rack para ODFs Reflejos (con nuevos ODFs)",
            "Proyeciones Bases antisismicas para Nuevos Racks",
            "Proyecciones Fijaciones Superior y/o Inferior para Nuevos Racks",
            "Proyección de Espacios Nuevos SubRacks en Rack Existente",
            "Proyección de Espacios Nuevos ODFs en Rack Existente",
            "Longitudes de Jumpers para Cableado Interno (cantidad x longitudes x color)",
            "Verificación Disponibilidad de Rack - ODF Línea si Aplica",
            "Longitudes de Jumpers para Cableado (ODFs de Línea a Plat. Transporte)",
            "Proyección y Disponibilidad en ODF Reflejos",
            "Longitudes de Jumpers para Cableado (ODFs de Reflejos a Plat. Transporte)",
            "Longitudes de Jumpers para Cableado (ODFs de Reflejos en Plat. Servicios)",
            "Verificación Disponibilidad en ODF de Interconexión",
            "Longitudes de Jumpers - Habilitación de Servicios (Transp. a Servicios)",
            "Proyección Sistemas de Escalerillas",
            "Proyección de Sistemas de Canaletas",
            "Ubicación de Sistemas de Energía (Team Imp)",
            "Verificación de la Barra a Tierra del sitio",
            "Proyección y Disponibilidad de Sistemas de Gestión",
            "Proyección para la Instalación de Pararrayos",
            "Proyección para la Instalación de Antena(s) GPS",
            "Longitud de Jumpers de Fibra Óptica para la Integración"
        ],
        'IDR': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Mediciones de Consumo",
            "Verificar Disponibilidad de Empalme",
            "Verificar Disponibilidad de Grupo Electrogeno",
            "Verificar Disponibilidad en Fuentes de CC",
            "Verificar Disponibilidad de Energía en Baterías",
            "Verificar Disponibilidad de Climatización",
            
        ]
    },
    
    'H1 - Instalación Parcial': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Instalación de Base Antisísmica. Si Aplica.",
            "Instalación Rack/Subrack (Plataforma de Datos y/o Transporte, Incluye Rack ODF si Aplica)",
            "Instalación de Escalerillas metálicas",
            "Instalación de Anclaje Superior e Inferior.",
            "Tendido y conexiones Eléctricas",
            "Adecuación de Rack",
            "Conexión a Barra de Tierra",
            "Instalación de Pararrayos",
            "Instalación de antena(s) GPS",
        ],
        'IDR': [
             
        ]
    },
    
    'H2.A - Instalación Final Plataforma de Servicio': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Adecuación de Frente de Equipo y/o Inserción de Nuevas Tarjetas en Equipos Existentes según diseño",
            "Cableados Internos",
            "Tendido de Gestión ",
            "Sistema de Canalización Óptica",
            "Instalación de Paneles y/o ODFs Locales/Reflejos en Rack Nuevo o Existente",
            "Tendido de Jumpers Ópticos a ODF Reflejos",
            "Supervisión de Power ON",
            "Configuración de Parámetros Básicos",
            "Cableados Internos",
        ],
        'IDR': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Mediciones de Consumo",
            "Instalación de Alimentadores",
            "Conexión de Alimentadores",
            "Ejecución de Power ON",
            "Intalación de Breakers",
            "Cambio de Breakers",
            "Pruebas de Redundancia",
            "Identificación de punto de aterramiento",
            
        ]
    },

    'H2.B - Instalación Final Plataforma de Transporte': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías del Sala",
            "Tendido de Jumpers Ópticos de Línea a ODF",
            "Conexiones ópticas y habilitación de enlace óptico",
        ],
        'IDR': []
    },

    'H3 - Habilitación de Capacidad (Lambdas y/o Reflejos)': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Opción 1: Tendido de jumpers para Habilitación Nva Lambda: desde lado DWDM a Dirección Local (Mux/Demux)",
            "Opción 2: Tendidos para Continuidad óptica de Lambdas (Entre puertos Mux/Demux entre 2 Direcciones Locales)",
            "Opción 3: Tendidos para Continuidad óptica a través de Lambda Alíen (Entre Lado DWDM (tarjeta de Línea o Transpondedor a puertos Mux/Demux de equipos en gestores diferentes)",
            "Opción 4: Tendidos para habilitación de Lambda Gris (lado de Línea Transpondedor a Puerta Cliente Tributaria)",
            "Apoyo en Creación de OCH y Ecualización de Lambdas",
            "Pruebas de Restauración de Lambdas ",
            "Pruebas de Conmutación de Servicios ",
            "Pruebas de Conmutación de tarjetas controladoras, si Aplica.",
            "Pruebas de Conmutación de Fuentes de Energía, solamente del lado del nuevo equipo y si Aplica",
            "Loop o Cascadas para mediciones",
            "Mediciones RFC y BERT",
        ],
        'IDR': []
    },

    'H4 - Habilitación de Servicios': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Tendidos y conexiones de fibra óptica a ODFs de Interconexión. Si Aplica",
            "Tendidos y Conexiones de fibra óptica a ODFs Reflejos Plataforma de Transporte",
            "Tendido de Jumpers de FO a Plataforma de Servicios (conexiones en lado ODF, no conectado en lado en lado Plataforma de servicios)",
            "Mediciones E2E",
        ],
        'IDR': []
    },

    'H4* -Integración/Ampliación Plataforma de Servicios': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Conexiones de jumpers en lado de la Plataforma de Servicios.",
            "Pruebas. Si Aplica",
        ],
        'IDR': []
    },

    'H5 - Migraciones': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Tendido de Jumpers Ópticos de Servicios",
            "Tendido de cable Coaxial",
            "Elaboración y Tendidos de Cables UTPs de Servicios",
            "Migración de Servicios",
        ],
        'IDR': []
    },

    'H6 - Desinstalación y Retiro': {
        'IMP': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías del Sala",
            "Supervición de Power OFF",
            "Retiro de Tendidos de Jumpers de Fibra Óptica",
            "Retiro de Tendidos de Cables de UTP",
            "Retiro de Cable Coaxial",
            "Retiros de Tarjetas (si Aplica)",
            "Retiro de Subrack",
            "Retiro de Rack",
        ],
        'IDR': [
            "Adjunto Fotografías del Sitio",
            "Adjunto Fotografías del Acceso",
            "Adjunto Fotografías de Sala",
            "Diagrama Layout de Planta",
            "Mediciones de Consumo",
            "Ejecución de Power OFF",
            "Desconexión de Alimentadores",
            "Retiro de Alimentadores",
        ]
    }
}

class AuditChecklistLine(models.Model):
    _name = "audit.checklist.line"
    _description = "Línea de Checklist de Auditoría"
    _order = "sequence, id"

    task_id = fields.Many2one('project.task', string="Tarea", ondelete='cascade')
    sequence = fields.Integer(string="Secuencia", default=10)
    
    name = fields.Char(string="Ítem a Evaluar", required=True)
    is_checked = fields.Boolean(string="¿Requerida?")
    is_realizado = fields.Boolean(string="¿Realizado?")

    user_id = fields.Many2one(
        'res.users', 
        string="Supervisor Revisor",
        default=lambda self: self.env.user
    )

    attachment_ids = fields.Many2many(
        'ir.attachment',
        string="Evidencias (Fotos)",
        help="Adjunte aquí una o varias fotografías de evidencia."
    )
    
    score = fields.Selection(
        [
            ('0', '0'),
            ('25', '25'),
            ('50', '50'),
            ('75', '75'),
            ('100', '100')
        ], 
        string="Puntaje", 
        default='0',
        required=True
    )

    observaciones = fields.Text(string="Observaciones")

    @api.onchange('is_checked')
    def _onchange_is_checked(self):
        if self.is_checked:
            self.user_id = self.env.user
        else:
            self.user_id = False

    def action_view_attachments(self):
        self.ensure_one()
        return {
            'name': 'Evidencias Fotográficas',
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'view_mode': 'kanban,form',
            'domain': [('res_model', '=', 'audit.checklist.line'), ('res_id', '=', self.id)],
            'context': {
                'default_res_model': 'audit.checklist.line', 
                'default_res_id': self.id,
                'create': True, 
            },
            'target': 'current',
        }

class ProjectTask(models.Model):
    _inherit = 'project.task'

    checklist_line_ids = fields.One2many(
        'audit.checklist.line', 
        'task_id', 
        string="Checklist de Auditoría"
    )

    audit_final_avg = fields.Float(
        string="Promedio Auditoría", 
        compute="_compute_audit_final_avg", 
        store=True,
        aggregator="avg"
    )

    # Nota: x_studio_hito y x_studio_area_interna son campos de Studio,
    # no necesitan re-declararse aquí si ya existen en la base de datos,
    # pero los usamos en la lógica.

    @api.depends('checklist_line_ids.score', 'checklist_line_ids.is_checked')
    def _compute_audit_final_avg(self):
        for record in self:
            active_items = record.checklist_line_ids.filtered(lambda x: x.is_checked)
            
            if active_items:
                total_score = sum(int(line.score or '0') for line in active_items)
                record.audit_final_avg = total_score / len(active_items)
            else:
                record.audit_final_avg = 0.0

    def action_load_audit_checklist(self):
        self.ensure_one()
        
        current_hito = self.x_studio_hito 
        current_area = self.x_studio_rea_interna 

        if not current_hito:
            raise UserError("Por favor seleccione un Hito antes de cargar el checklist.")
        
        if not current_area:
            raise UserError("Por favor seleccione el Área Interna (IMP o IDR) antes de cargar el checklist.")

        hito_data = AUDIT_QUESTIONS.get(current_hito, {})
             
        master_questions = hito_data.get(current_area, [])

        if not master_questions:
        
            return

        existing_names = self.checklist_line_ids.mapped('name')

        new_lines = []
        
        for index, question in enumerate(master_questions):
            if question not in existing_names:
                new_lines.append({
                    'task_id': self.id,
                    'name': question,
                    'sequence': index + 1, 
                    'is_checked': False,
                    'score': '0'
                })
        
        if new_lines:
            self.env['audit.checklist.line'].create(new_lines)

    def action_clean_audit_checklist(self):
        self.ensure_one()
        self.checklist_line_ids.unlink()

    def action_remove_unchecked_audit_lines(self):
        """ Elimina las líneas del checklist donde is_checked es False """
        self.ensure_one()
        # Filtramos las líneas que NO están marcadas como requeridas
        lines_to_remove = self.checklist_line_ids.filtered(lambda l: not l.is_checked)
        lines_to_remove.unlink()