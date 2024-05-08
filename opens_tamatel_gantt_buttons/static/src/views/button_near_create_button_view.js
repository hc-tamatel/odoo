/** @odoo-module */

import { ganttView } from "@web_gantt/gantt_view";
import { registry } from "@web/core/registry";
import { ButtonNearCreateButtonController as Controller } from './button_near_create_button_controller';

export const ButtonNearCreateButtonView = {
    ...ganttView,
    Controller,
    buttonTemplate: 'd_button_near_create_button.ButtonNearCreateButtonView.Buttons',
};

registry.category("views").add("button_near_create_button", ButtonNearCreateButtonView);
