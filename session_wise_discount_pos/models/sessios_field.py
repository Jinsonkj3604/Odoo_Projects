from odoo import models, fields

class SessionField(models.Model):
    _inherit = "pos.config"
    _description = "Session Field In Pos"

    session_disc = fields.Boolean(string="Session Discount Limit", default=False)
    maxim_discount = fields.Float(string="Session Discount")
    catg_id = fields.Many2one("pos.category", string="Discount Category")

