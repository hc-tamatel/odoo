/** @odoo-module */

import { Component, useState, onWillDestroy, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class AuditTimerField extends Component {
    static template = "admin_task_audit.AuditTimerField";
    static props = {
        ...standardFieldProps,
    };

    setup() {
        this.state = useState({
            displayTime: this.props.record.data.display_duration || "00:00:00",
        });

        this.interval = null;

        onMounted(() => {
            this._startTimer();
        });

        onWillDestroy(() => {
            this._clearTimer();
        });
    }

    _startTimer() {
        // Run update immediately then interval
        this._updateTime();
        this.interval = setInterval(() => {
            this._updateTime();
        }, 1000);
    }

    _clearTimer() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
    }

    _updateTime() {
        const record = this.props.record.data;
        const timerState = record.timer_state;

        // Si está parado o pausado, mostrar lo que viene del backend (record.display_duration)
        // Pero si queremos que sea 'smooth' incluso al pausar, mejor recálculo local si es running.

        if (timerState !== 'running' || !record.timer_start) {
            this.state.displayTime = record.display_duration || "00:00:00";
            return;
        }

        // Si está corriendo, calculamos live
        // timer_start es un objeto luxon DateTime en Odoo moderno
        const startTime = record.timer_start;
        const accumulatedDuration = record.duration || 0.0; // minutos

        if (!startTime) return;

        // Diferencia en ms
        // Nota: Odoo usa luxon.DateTime para fechas. 
        // Si startTime es string, convertir. Pero en OWL fields suele ser objeto.
        // Asumimos luxon (standard en Odoo 16+)

        const now = luxon.DateTime.now();
        const start = typeof startTime === 'string' ? luxon.DateTime.fromISO(startTime) : startTime;

        const diffInSeconds = now.diff(start, 'seconds').seconds;

        const totalMinutes = accumulatedDuration + (diffInSeconds / 60.0);

        // Convert a HH:MM:SS
        const totalSeconds = Math.floor(totalMinutes * 60);

        const hours = Math.floor(totalSeconds / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        const seconds = totalSeconds % 60;

        const pad = (n) => n.toString().padStart(2, '0');
        this.state.displayTime = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
    }
}

export const auditTimerField = {
    component: AuditTimerField,
    supportedTypes: ["char"],
};

registry.category("fields").add("audit_timer", auditTimerField);
