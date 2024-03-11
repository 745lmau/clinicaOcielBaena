from odoo import api, fields, models


class ClinicAI(models.Model):
    _name = "clinic.ai"

    name = fields.Char()
    partner_id = fields.Many2one(
        comodel_name="res.partner",
    )
    contraction_id = fields.Many2one(
        comodel_name="disease.contraction",
        domain="[('partner_id', '=', partner_id)]"
    )
    risk_points = fields.Integer()
    risk_details = fields.Char()
    suggested_treatment = fields.Char()

    @api.onchange("risk_points")
    def set_risk_points(self):
        for record in self:
            record.partner_id.risk_points = record.risk_points

    @api.onchange("risk_details")
    def set_risk_details(self):
        for record in self:
            record.partner_id.risk_details = record.risk_details

    @api.onchange("suggested_treatment")
    def set_suggested_treatment(self):
        for record in self:
            record.partner_id.suggested_treatment = record.suggested_treatment

    def action_compute_risk_data(self):
        pass

    def action_compute_suggested_treatment(self):
        pass
