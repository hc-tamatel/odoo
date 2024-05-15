/** @odoo-module */

import { useService } from "@web/core/utils/hooks";
import { GanttController } from "@web_gantt/gantt_controller";

export class ButtonNearCreateButtonController extends GanttController {
	setup() {
		super.setup();
		this.orm = useService("orm");
	}

	async customGroup1() {
//		await this.orm.call('project.task', 'action_open_gantt_task_view', [], {}); // this one call a python method that we define in the project model
		const action = await this.orm.call('project.task', 'custom_group_1', [], {'context': this.props.context});
        this.actionService.doAction(action);
//		await this.model.root.load();
//		this.model.notify();
	}

		async customGroup2() {
//		await this.orm.call('project.task', 'action_open_gantt_task_view', [], {}); // this one call a python method that we define in the project model
		const action = await this.orm.call('project.task', 'custom_group_2', [], {'context': this.props.context});
        this.actionService.doAction(action);
//		await this.model.root.load();
//		this.model.notify();
	}

		async customGroup3() {
//		await this.orm.call('project.task', 'action_open_gantt_task_view', [], {}); // this one call a python method that we define in the project model
		const action = await this.orm.call('project.task', 'custom_group_3', [], {'context': this.props.context});
        this.actionService.doAction(action);
//		await this.model.root.load();
//		this.model.notify();
	}
}
