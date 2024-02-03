from odoo.addons.hr_attendance.controllers.main import HrAttendance


class ProjectHrAttendance(HrAttendance):
    @staticmethod
    def _get_employee_info_response(employee):
        res = HrAttendance._get_employee_info_response(employee)
        if res:
            res.update(
                {
                    "project_id": employee.last_attendance_id.project_id.id,
                    "task_id": employee.last_attendance_id.task_id.id,
                }
            )

        return res
