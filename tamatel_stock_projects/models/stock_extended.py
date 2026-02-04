from odoo import models, fields, api
from odoo.tools import float_compare, float_is_zero

# ---------------------------------------------------------
# 1. STOCK PICKING (Albarán)
# ---------------------------------------------------------
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tm_macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')
    tm_project_id = fields.Many2one('tm.project', string='Proyecto')
    tm_subproject_id = fields.Many2one('tm.subproject', string='Subproyecto')
    tm_site_id = fields.Many2one('tm.site', string='Sitio')


# ---------------------------------------------------------
# 2. STOCK MOVE
# ---------------------------------------------------------
class StockMove(models.Model):
    _inherit = 'stock.move'

    tm_macro_project_id = fields.Many2one(
        'tm.macro.project', related='picking_id.tm_macro_project_id', store=True, string='Macro Proyecto')
    tm_project_id = fields.Many2one(
        'tm.project', related='picking_id.tm_project_id', store=True, string='Proyecto')
    tm_subproject_id = fields.Many2one(
        'tm.subproject', related='picking_id.tm_subproject_id', store=True, string='Subproyecto')
    tm_site_id = fields.Many2one(
        'tm.site', related='picking_id.tm_site_id', store=True, string='Sitio')

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super(StockMove, self)._prepare_move_line_vals(quantity=quantity, reserved_quant=reserved_quant)
        vals.update({
            'tm_macro_project_id': self.tm_macro_project_id.id,
            'tm_project_id': self.tm_project_id.id,
            'tm_subproject_id': self.tm_subproject_id.id,
            'tm_site_id': self.tm_site_id.id,
        })
        return vals


# ---------------------------------------------------------
# 3. STOCK MOVE LINE
# ---------------------------------------------------------
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    tm_macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')
    tm_project_id = fields.Many2one('tm.project', string='Proyecto')
    tm_subproject_id = fields.Many2one('tm.subproject', string='Subproyecto')
    tm_site_id = fields.Many2one('tm.site', string='Sitio')

    def _action_done(self):
        for line in self:
            context_vals = {
                'default_tm_macro_project_id': line.tm_macro_project_id.id,
                'default_tm_project_id': line.tm_project_id.id,
                'default_tm_subproject_id': line.tm_subproject_id.id,
                'default_tm_site_id': line.tm_site_id.id,
            }
            super(StockMoveLine, line.with_context(**context_vals))._action_done()
        return True


# ---------------------------------------------------------
# 4. STOCK QUANT (CORREGIDO)
# ---------------------------------------------------------
class StockQuant(models.Model):
    _inherit = 'stock.quant'

    tm_macro_project_id = fields.Many2one('tm.macro.project', string='Macro Proyecto')
    tm_project_id = fields.Many2one('tm.project', string='Proyecto')
    tm_subproject_id = fields.Many2one('tm.subproject', string='Subproyecto')
    tm_site_id = fields.Many2one('tm.site', string='Sitio')

    @api.model
    def _get_inventory_fields_create(self):
        res = super(StockQuant, self)._get_inventory_fields_create()
        res.extend(['tm_macro_project_id', 'tm_project_id', 'tm_subproject_id', 'tm_site_id'])
        return res

    @api.model
    def _update_available_quantity(self, product_id, location_id, quantity, lot_id=None, package_id=None, owner_id=None, strict=False, allow_negative=False, in_date=None):
        """
        Sobrescribimos para incluir proyectos y retornar la tupla (qty, in_date) correcta.
        """
        tm_macro = self.env.context.get('default_tm_macro_project_id')
        tm_project = self.env.context.get('default_tm_project_id')
        tm_subproject = self.env.context.get('default_tm_subproject_id')
        tm_site = self.env.context.get('default_tm_site_id')
        
        # Odoo espera devolver una tupla si quantity es 0
        if float_is_zero(quantity, precision_rounding=product_id.uom_id.rounding):
            return 0.0, in_date # Importante: retornar tupla también aquí

        self = self.sudo()
        quants = self._gather(product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict)
        
        if strict:
            quants = quants.filtered(lambda q: 
                q.tm_macro_project_id.id == tm_macro and
                q.tm_project_id.id == tm_project and
                q.tm_subproject_id.id == tm_subproject and
                q.tm_site_id.id == tm_site
            )
        else:
            candidate = quants.filtered(lambda q: 
                q.tm_macro_project_id.id == tm_macro and
                q.tm_project_id.id == tm_project and
                q.tm_subproject_id.id == tm_subproject and
                q.tm_site_id.id == tm_site
            )
            if candidate:
                quants = candidate

        quant = quants and quants[0] or False
        
        if not quant:
            # Si in_date es None, asignamos la fecha actual para crear el registro
            # y actualizamos la variable local para devolverla correctamente al final.
            in_date = in_date or fields.Datetime.now()
            
            vals = {
                'product_id': product_id.id,
                'location_id': location_id.id,
                'lot_id': lot_id and lot_id.id,
                'package_id': package_id and package_id.id,
                'owner_id': owner_id and owner_id.id,
                'quantity': quantity,
                'in_date': in_date,
                'tm_macro_project_id': tm_macro,
                'tm_project_id': tm_project,
                'tm_subproject_id': tm_subproject,
                'tm_site_id': tm_site,
            }
            quant = self.create(vals)
        else:
            quant.quantity += quantity
            # Si es una actualización, in_date se mantiene como viene (o None)
            
        # Obtenemos la cantidad final disponible
        available_qty = quant._get_available_quantity(product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict, allow_negative=allow_negative)
        
        # CORRECCIÓN FINAL: Retornamos la tupla (cantidad, fecha)
        return available_qty, in_date