/** @odoo-module */

import { useService } from "@web/core/utils/hooks";
import { GanttController } from "@web_gantt/gantt_controller";


export class ButtonNearCreateButtonController extends GanttController {
	setup() {
		super.setup();
		this.orm = useService("orm");
	}

	async customGroup1() {
		const groupName = await this.orm.call('project.task', 'custom_group_1', [],);
//        this.actionService.doAction(action);
        const filter = this.env.searchModel.getSearchItems().filter(item => item.fieldName == groupName && item.type == 'groupBy');
        this.env.searchModel.toggleSearchItem(filter[0].id);

//		await this.model.root.load();
//		this.model.notify();
	}

		async customGroup2() {
		const groupName = await this.orm.call('project.task', 'custom_group_2', [],);
		const filter = this.env.searchModel.getSearchItems().filter(item => item.fieldName == groupName && item.type == 'groupBy');
        this.env.searchModel.toggleSearchItem(filter[0].id);

	}

		async customGroup3() {
		const action = await this.orm.call('project.task', 'custom_group_3', [], {'context': this.props.context});
        this.actionService.doAction(action);

	}
}
