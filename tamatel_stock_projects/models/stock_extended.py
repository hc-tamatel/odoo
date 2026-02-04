from odoo import models, fields, api

# ---------------------------------------------------------
# 1. STOCK PICKING (Albarán) - Entrada de datos
# ---------------------------------------------------------
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tm_macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')
    tm_project_id = fields.Many2one('tm.project', string='Proyecto')
    tm_subproject_id = fields.Many2one('tm.subproject', string='Subproyecto')
    tm_site_id = fields.Many2one('tm.site', string='Sitio')


# ---------------------------------------------------------
# 2. STOCK MOVE (El puente)
# ---------------------------------------------------------
class StockMove(models.Model):
    _inherit = 'stock.move'

    # Usamos 'related' con store=True para que se copie automáticamente del Picking al Move
    tm_macro_project_id = fields.Many2one(
        'tm.macro.project', related='picking_id.tm_macro_project_id', store=True, string='Macro Proyecto')
    tm_project_id = fields.Many2one(
        'tm.project', related='picking_id.tm_project_id', store=True, string='Proyecto')
    tm_subproject_id = fields.Many2one(
        'tm.subproject', related='picking_id.tm_subproject_id', store=True, string='Subproyecto')
    tm_site_id = fields.Many2one(
        'tm.site', related='picking_id.tm_site_id', store=True, string='Sitio')

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        """
        Interceptamos la creación de la línea de movimiento para inyectar nuestros proyectos.
        Sin esto, el dato no llega al Quant.
        """
        vals = super(StockMove, self)._prepare_move_line_vals(quantity=quantity, reserved_quant=reserved_quant)
        
        # Agregamos nuestros campos al diccionario de valores
        vals.update({
            'tm_macro_project_id': self.tm_macro_project_id.id,
            'tm_project_id': self.tm_project_id.id,
            'tm_subproject_id': self.tm_subproject_id.id,
            'tm_site_id': self.tm_site_id.id,
        })
        return vals


# ---------------------------------------------------------
# 3. STOCK MOVE LINE (Detalle del movimiento)
# ---------------------------------------------------------
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    tm_macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')
    tm_project_id = fields.Many2one('tm.project', string='Proyecto')
    tm_subproject_id = fields.Many2one('tm.subproject', string='Subproyecto')
    tm_site_id = fields.Many2one('tm.site', string='Sitio')


# ---------------------------------------------------------
# 4. STOCK QUANT (El inventario físico) - ¡CRÍTICO!
# ---------------------------------------------------------
class StockQuant(models.Model):
    _inherit = 'stock.quant'

    tm_macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')
    tm_project_id = fields.Many2one('tm.project', string='Proyecto')
    tm_subproject_id = fields.Many2one('tm.subproject', string='Subproyecto')
    tm_site_id = fields.Many2one('tm.site', string='Sitio')

    @api.model
    def _get_inventory_fields_create(self):
        """
        Esta función define qué campos hacen que un stock sea único.
        Al agregar nuestros proyectos aquí, Odoo NO mezclará inventario de diferentes proyectos.
        """
        res = super(StockQuant, self)._get_inventory_fields_create()
        # Agregamos los campos a la clave de unicidad del stock
        res += ['tm_macro_project_id', 'tm_project_id', 'tm_subproject_id'],['tm_site_id']
        return res