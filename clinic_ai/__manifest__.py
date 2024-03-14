{
    "name": "Clinic AI",
    "version": "17.0.0.0.1",  # standard: start with Odoo version
    "author": "Mauricio Pastrana Macias, Bernardo Muñoz Escoto",
    "category": "Health",
    "module_type": "clinic",
    "description": """
    This is an AI tool that estimates risk points for a clinic's patients
    Especifically made for OB Clinic
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/clinic_ai.xml",
        "views/res_company.xml",
    ],
    "depends": [
        "ob_clinic",
    ],
}
