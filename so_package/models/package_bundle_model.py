from AptUrl.Helpers import _

from odoo import fields, models, api


class PackBundle(models.Model):
    _name = "sale.package.bundle"
    _description = "sale package Bundle"
    _rec_name = "seq_no"

    s_refer = fields.Char(string="Sale order reference")
    date = fields.Date(string="Date")
    ex_date = fields.Date(string="Expected Date")
    partner_id = fields.Many2one("res.partner", string="Partner")
    weight = fields.Integer(string="weight")
    height = fields.Integer(string="height")
    length = fields.Integer(string="length")
    width = fields.Integer(string="width")
    product_id = fields.Many2one("product.product", string="Product")
    quantity = fields.Char(string="Quantity")
    name = fields.Char(string="Name Of Package")
    seq_no = fields.Char(string='Order Reference', required=True,
                         readonly=True, default=lambda self: _('New'))
    person_id = fields.Many2one("res.users", string="sales person")

    page_ids = fields.One2many('sale.package.bundle.page', "packs_id", string="Package Details")



    @api.model
    def create(self, vals):
        if vals.get('seq_no', _('New')) == _('New'):
            vals['seq_no'] = self.env['ir.sequence'].next_by_code(
                'sale.package.bundle') or _('New')
        res = super(PackBundle, self).create(vals)
        return res



