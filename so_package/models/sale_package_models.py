from odoo import fields, models


class SalePack(models.Model):
    _name = "sale.package.model"
    _description = "sale packages"

    name = fields.Char(string="Name", required=True)
    width = fields.Integer(string="width", required=True)
    height = fields.Integer(string="height", required=True)
    length = fields.Integer(string="length", required=True)
    m_weight = fields.Integer(string="maximum_weight", required=True)
    sale_id = fields.Many2one("sale.order")







