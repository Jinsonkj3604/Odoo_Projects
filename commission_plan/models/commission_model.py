from odoo import fields, models, api, _


class CrmCommission(models.Model):
    _name = "crm.commission"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "crm commission"

    commission = fields.Char(string="Name", required=True)
    from_date = fields.Date(string="From date")
    to_date = fields.Date(string="To date")
    type = fields.Selection(selection=[('pw', 'product wise'), ('rw', 'revenue wise')], string="Type", required=True,
                            default='pw')
    revenue_type = fields.Selection(selection=[('straight', 'Straight'), ('graduate', 'Graduate')], string="Type")
    active = fields.Boolean(default=True)
    products_ids = fields.One2many('product.wise.model', 'item_id')
    revenues_ids = fields.One2many('revenue.wise.model', 'revenue_id')
    status = fields.Selection(selection=[('draft', 'Draft'), ('running', 'Running'), ('cancel', ' Cancel')],
                              default='draft', tracking=True)
    name = fields.Char(string='sequence', required=True, readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'crm.commission') or _('New')
        res = super(CrmCommission, self).create(vals)
        return res

    def action_cancel(self):
        self.write({
            'status': 'cancel',
            'active': False
        })
        

class InheritCommission(models.Model):
    _inherit = "crm.commission"
    
    @api.model
    def create(self, vals):
        vals['status'] = 'running'
        return super(InheritCommission, self).create(vals)


class ProductWise(models.Model):
    _name = "product.wise.model"
    _description = "Product wise model"

    cat_id = fields.Many2one("product.category", string="Product Category")
    product_id = fields.Many2one("product.product", string="Product", domain="[('categ_id', '=', cat_id)]")
    rate = fields.Float(string="Rate")
    max_com = fields.Float(string="Maximum Commission Amount")
    item_id = fields.Many2one('crm.commission')


class RevenueWise(models.Model):
    _name = "revenue.wise.model"
    _description = "Revenue Wise Commission"

    from_amt = fields.Integer(string="From amount")
    to_amt = fields.Integer(string="To amount")
    rate = fields.Float(string="rate")

    revenue_id = fields.Many2one('crm.commission')


class SalesTeamInherited(models.Model):
    _inherit = "crm.team"
    _description = "inherited field"

    crm_id = fields.Many2one("crm.commission", string="Commission")


class TeamMemberInherited(models.Model):
    _inherit = "crm.team.member"
    _description = "member inherited field"

    member_id = fields.Many2one("crm.commission", string="Commission")


class SalesPersonInherited(models.Model):
    _inherit = "sale.order"
    _description = "inherited sale order field"

    sale_id = fields.Many2one(string="Commission", related="team_id.crm_id")
    commission = fields.Float(string="Commission")

    @api.model
    def action_confirm(self):
        res = super(SalesPersonInherited, self).action_confirm()
        commission = self.sale_id.type
        amount = self.amount_total
        if commission == 'rw':
            type = self.sale_id.revenue_type
            if type == 'straight':
                for rec in self.sale_id.revenues_ids:
                    for dec in rec:
                        f_amt = dec.from_amt
                        t_amt = dec.to_amt

                        if (amount >= f_amt) and (amount <= t_amt):
                            rate = dec.rate
                            compute = (amount * rate) / 100
                            self.commission = compute

            elif type == 'graduate':
                comp = 0
                for rec in self.sale_id.revenues_ids:
                    for dec in rec:
                        f_amt = dec.from_amt
                        t_amt = dec.to_amt
                        rate = dec.rate
                        print(f_amt, t_amt, rate)
                        if amount > t_amt:
                            comp = (t_amt * rate) / 100
                            amount = amount - t_amt
                        else:
                            compute = comp + (amount * dec.rate) / 100
                            self.commission = compute

        else:
            if commission == 'pw':
                commission_amount = 0
                compute = 0
                for rec in self.order_line:
                    for c_product in self.sale_id.products_ids:
                        for product in c_product:
                            if rec.product_id == product.product_id:
                                price = rec.price_subtotal
                                rate = product.rate
                                compute = (price * (rate / 100))
                                commission_amount = compute + commission_amount
                                if compute > product.max_com:
                                    comp = product.max_com
                                    compute = comp
                                    commission_amount = compute

                self.commission = commission_amount
        return res
