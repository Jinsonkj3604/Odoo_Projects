from odoo import fields, models, api


class InheritModel(models.Model):
    _inherit = "sale.order"

    package_ids = fields.Many2many("sale.package.model", string="Package")
    pack_ids = fields.One2many('sale.package.model', "sale_id", string="Package")

    @api.onchange('package_ids')
    def _onchange_package_ids(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.package_ids:
                values = {
                    'name': line.name,
                    'width': line.width,
                    'height': line.height,
                    'length': line.length,
                    'm_weight': line.m_weight,
                }
                lines.append((0, 0, values))
            rec.pack_ids = lines

    # creating package bundle record

    def action_confirm(self):
        res = super(InheritModel, self).action_confirm()
        bundle = self.env['sale.package.bundle'].create({
            # 'reference_id': self.name,
            'partner_id': self.partner_id.id,
            'date': self.date_order,
            'ex_date': self.validity_date,
            's_refer': self.name,
            'person_id': self.user_id.id
        })

        if self.order_line:
            for i in self.order_line:
                self.env['sale.package.bundle.page'].create({
                    'name': i.package_field.name,
                    'product_id': i.product_id.id,
                    'quantity': i.product_uom_qty,
                    'weight': i.package_field.m_weight,
                    'height': i.package_field.height,
                    'width': i.package_field.width,
                    'length': i.package_field.length,
                    'packs_id': bundle.id
                })

                return res


class InheritModel1(models.Model):
    _inherit = "sale.order.line"

    package_field = fields.Many2one("sale.package.model", string="pack")


# smart button
class SmartButton(models.Model):
    _inherit = "stock.picking"

    def package_bundle(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bundles',
            'view_mode': 'tree',
            'res_model': 'sale.package.bundle',
            'domain': [('s_refer', '=', self.origin)],
            'context': "{'create': False}"
        }


