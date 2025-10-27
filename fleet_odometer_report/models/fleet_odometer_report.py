# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

class FleetOdometerReport(models.Model):
    _name = 'fleet.odometer.report'
    _description = 'Reporte de Odómetro por Vehículo/Conductor'
    _auto = False
    _rec_name = 'vehicle_id'

    date = fields.Date(string='Fecha')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehículo', index=True)
    license_plate = fields.Char(string='Patente', index=True)
    driver_id = fields.Many2one('res.partner', string='Conductor', index=True)
    driver_name = fields.Char(string='Nombre Conductor', index=True)
    axis_driver_or_plate = fields.Char(string='Conductor/Patente (X)', index=True)

    # NUEVO: valor absoluto del odómetro (en km)
    odometer_km = fields.Float(string='Odómetro (km)')

    # (Opcional) mantén distancia para otros reportes
    distance_km = fields.Float(string='Distancia (km)')

    def _select(self):
        return """
            SELECT
                row_number() OVER () AS id,
                d.reading_date::date AS date,
                d.vehicle_id AS vehicle_id,
                v.license_plate AS license_plate,
                v.driver_id AS driver_id,
                rp.name AS driver_name,
                COALESCE(rp.name, v.license_plate) AS axis_driver_or_plate,

                -- Valor absoluto del odómetro normalizado a KM
                CASE
                    WHEN COALESCE(v.odometer_unit, 'kilometers') IN ('kilometers','km') THEN d.value
                    WHEN COALESCE(v.odometer_unit, 'kilometers') IN ('miles','mi') THEN d.value * 1.609344
                    ELSE d.value
                END AS odometer_km,

                -- Distancia recorrida entre lecturas (por si la usas en otro reporte)
                CASE
                    WHEN COALESCE(v.odometer_unit, 'kilometers') IN ('kilometers','km') THEN COALESCE(d.delta_val, 0)
                    WHEN COALESCE(v.odometer_unit, 'kilometers') IN ('miles','mi') THEN COALESCE(d.delta_val, 0) * 1.609344
                    ELSE COALESCE(d.delta_val, 0)
                END AS distance_km

            FROM (
                SELECT
                    o.id,
                    o.vehicle_id,
                    o.date AS reading_date,
                    o.value AS value,
                    GREATEST(
                        0,
                        o.value - LAG(o.value) OVER (
                            PARTITION BY o.vehicle_id
                            ORDER BY o.date, o.id
                        )
                    ) AS delta_val
                FROM fleet_vehicle_odometer o
            ) d
            LEFT JOIN fleet_vehicle v ON v.id = d.vehicle_id
            LEFT JOIN res_partner rp ON rp.id = v.driver_id
        """

    def _from(self):
        return ""

    def _group_by(self):
        return ""

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute(f"""
            CREATE OR REPLACE VIEW {self._table} AS (
                {self._select()}
            )
        """)
