{
    "name": "Project Attendances",
    "version": "1.0",
    "category": "Human Resources/Attendances",
    "summary": "Track employee attendance via project",
    "description": """
This module aims to manage employee's attendances via projects/tasks.
==================================================

Keeps account of the attendance via the project of the employees based 
on the actions(Check-in/Check-out) performed by them.
       """,
    "depends": ["hr_attendance", "project"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_attendance_views.xml",
        "wizard/hr_attendance_project_description_views.xml",
    ],
    "demo": ["data/hr_attendance_project_demo.xml"],
    "installable": True,
    "application": False,
    "pre_init_hook": "pre_init_check",
    "assets": {
        "web.assets_backend": [
            "hr_attendance_project/static/src/js/attendance_menu.js",
        ],
    },
    "license": "LGPL-3",
}
