from odoo import fields, models, api


class PackInfoPage(models.Model):
    _name = "sale.package.bundle.page"
    _description = "sale package bundle"

    weight = fields.Integer(string="weight")
    height = fields.Integer(string="height")
    length = fields.Integer(string="length")
    width = fields.Integer(string="width")
    product_id = fields.Many2one('product.product', string="Product")
    quantity = fields.Char(string="Quantity")
    name = fields.Char(string="Name Of Package")
    packs_id = fields.Many2one('sale.package.bundle')





