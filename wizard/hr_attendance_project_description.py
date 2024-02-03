from odoo import models, fields

from odoo.addons.hr_attendance.controllers.main import HrAttendance


class HrAttendanceProjectDescription(models.TransientModel):
    # ------------------------------------------------------------------
    # 1. PRIVATE ATTRIBUTES
    # ------------------------------------------------------------------

    _name = "hr.attendance.project.description"
    _description = "Project description in attendance"

    # ------------------------------------------------------------------
    # 2. DEFAULT METHODS AND default_get
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 3. FIELD DECLARATIONS
    # ------------------------------------------------------------------

    project_id = fields.Many2one("project.project", "Project", required=True)
    task_id = fields.Many2one(
        "project.task",
        "Task",
        domain="[('project_id', '=', project_id)]",
        required=True,
    )
    check_in_description = fields.Text("Check in Description")
    check_out_description = fields.Text("Check out Description")
    attendance_state = fields.Selection(
        [
            ("checked_out", "Checked out"),
            ("checked_in", "Checked in"),
        ],
        "Attendance Status",
        readonly=True,
    )
    latitude = fields.Float("Latitude", digits=(10, 7), readonly=True)
    longitude = fields.Float("Longitude", digits=(10, 7), readonly=True)

    # ------------------------------------------------------------------
    # 4. COMPUTE, INVERSE AND SEARCH METHODS
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 5. SELECTION METHODS
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 6. CONSTRAINS METHODS AND ONCHANGE METHODS
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 7. CRUD METHODS
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 8. ACTION METHODS
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 9. BUSINESS METHODS
    # ------------------------------------------------------------------

    def action_checkin_checkout(self):
        latitude = self.latitude or False
        longitude = self.longitude or False
        res = HrAttendance().systray_attendance(latitude, longitude)
        if res and res["attendance_state"] == "checked_in":
            employee = self.env["hr.employee"].browse(res["id"])
            employee.last_attendance_id.write(
                {
                    "project_id": self.project_id.id,
                    "task_id": self.task_id.id,
                    "check_in_description": self.check_in_description,
                }
            )
        elif res and res["attendance_state"] == "checked_out":
            employee = self.env["hr.employee"].browse(res["id"])
            employee.last_attendance_id.write(
                {"check_out_description": self.check_out_description}
            )

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
