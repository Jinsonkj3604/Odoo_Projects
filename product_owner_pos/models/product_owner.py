from odoo import models, fields


class ProductOwner(models.Model):
    _inherit = "product.template"

    owner_id = fields.Many2one("res.partner", string="Product Owner")
