/** @odoo-module */

import { useService } from "@web/core/utils/hooks";
import { GanttController } from "@web_gantt/gantt_controller";


export class ButtonNearCreateButtonController extends GanttController {

       async setup() {
        super.setup();
        this.orm = useService("orm");
        this.buttonClass1 = 'btn btn-secondary';
        this.buttonClass2 = 'btn btn-secondary';

        // Cachear nombres de grupos
        this.groupName1 = await this.getGroupName1();
        this.groupName2 = await this.getGroupName2();

        // Sobreescribir el método de cambio en la barra de búsqueda
        const originalToggleSearchItem = this.env.searchModel.toggleSearchItem;
        this.env.searchModel.toggleSearchItem = async (itemId) => {
            await originalToggleSearchItem.call(this.env.searchModel, itemId);
            this.updateButtonClasses();
        };

        // También sobrescribir los métodos que manejan la eliminación de etiquetas
        const originalDeactivateGroup = this.env.searchModel.deactivateGroup;
        this.env.searchModel.deactivateGroup = async (itemId) => {
            await originalDeactivateGroup.call(this.env.searchModel, itemId);
            this.updateButtonClasses();
        };
    }

    async getGroupName1() {
        const groupName = await this.orm.call('project.task', 'custom_group_1', [],);
        return groupName;
    }

    async getGroupName2() {
        const groupName = await this.orm.call('project.task', 'custom_group_2', [],);
        return groupName;
    }

    async customGroup1() {
        const groupName = this.groupName1;

        const filter = this.env.searchModel.getSearchItems().find(item => item.fieldName == groupName && item.type == 'groupBy');
        if (filter) {
            this.env.searchModel.toggleSearchItem(filter.id);
        }
    }

    async customGroup2() {
        const groupName = this.groupName2;

        const filter = this.env.searchModel.getSearchItems().find(item => item.fieldName == groupName && item.type == 'groupBy');
        if (filter) {
            this.env.searchModel.toggleSearchItem(filter.id);
        }
    }

    async updateButtonClasses() {
        const [groupName1, groupName2] = await Promise.all([this.getGroupName1(), this.getGroupName2()]);

        const filter1 = this.env.searchModel.getSearchItems().find(item => item.fieldName == groupName1 && item.type == 'groupBy');
        if (filter1) {
            this.buttonClass1 = filter1.isActive ? 'btn btn-primary' : 'btn btn-secondary';
        }

        const filter2 = this.env.searchModel.getSearchItems().find(item => item.fieldName == groupName2 && item.type == 'groupBy');
        if (filter2) {
            this.buttonClass2 = filter2.isActive ? 'btn btn-primary' : 'btn btn-secondary';
        }
    }

}
