from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    openai_token = fields.Char()
