{  # type: ignore
    "name": "Estados de Aprobación",
    "version": "0.1",
    "depends": ["base", "module_requester"],
    "author": "NePinFe",
    "data": [
        "data/approval_status_type_data.xml",
        "security/ir.model.access.csv",
        "views/type_views/approval_status_type_views.xml",
        "views/log_views/approval_status_log_views.xml",
        "views/approval_status_menu.xml",
        "views/log_views/approval_status_log_list.xml",
        "views/type_views/approval_status_type_list.xml",
        "views/type_views/approval_status_type_form.xml",
        "views/log_views/approval_status_log_form.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}