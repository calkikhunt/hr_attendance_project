/* @odoo-module */

import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
import { patch } from "@web/core/utils/patch";

patch(ActivityMenu.prototype, {
    async signInOut() {
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(
                async ({coords: {latitude, longitude}}) => {
                    this.env.services.action.doAction("hr_attendance_project.hr_attendance_project_description_action_view", 
                        {
                            additionalContext:{
                                'default_attendance_state': this.employee.attendance_state,
                                'default_project_id': this.employee.project_id,
                                'default_task_id': this.employee.task_id,
                                'default_latitude': latitude,
                                'default_longitude': longitude,
                            },
                        }
                    );
                },
                async err => {
                    this.env.services.action.doAction("hr_attendance_project.hr_attendance_project_description_action_view", 
                        {
                            additionalContext:{
                                'default_attendance_state': this.employee.attendance_state,
                                'default_project_id': this.employee.project_id,
                                'default_task_id': this.employee.task_id,
                            },
                        }
                    );
                }
            )
        }
        else{
            this.env.services.action.doAction("hr_attendance_project.hr_attendance_project_description_action_view", 
                {
                    additionalContext:{
                        'default_attendance_state': this.employee.attendance_state,
                        'default_project_id': this.employee.project_id,
                        'default_task_id': this.employee.task_id,
                    },
                }
            );
        }
    }
});
