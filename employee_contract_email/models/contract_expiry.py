from odoo import models, fields,api
from datetime import datetime
# import time


class ExpiryDateField(models.TransientModel):
    _inherit = "res.config.settings"
#
    end_date = fields.Integer(string="Expiry Days")

    def set_values(self):
        super(ExpiryDateField, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'employee_contract_email.end_date', self.end_date)

    @api.model
    def get_values(self):
        res = super(ExpiryDateField, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            end_date=params.get_param('employee_contract_email.end_date')
        )
        print(res['end_date'],"limit date")
        return res


class ContractExpiryEmail(models.Model):
    _inherit = "hr.contract"

    is_send = fields.Boolean("Send an Expire Contract Reminder", help="when it checked an contract expiration "
                                                                      "email send to the Hr responsible")

    def cron_demo_method(self):
        print(11)
        current = datetime.now()
        current = current.date()
        records = self.env['hr.contract'].search([])
        limit_date = self.env['res.config.settings'].search([])
        expire_limit = self.env['ir.config_parameter'].get_param('employee_contract_email.end_date')
        expire_limit = int(expire_limit)
        print(expire_limit,"current limit")

        for data in records:
            date = data.date_end
            if data.is_send == True:
                if date != False:
                    diff = (date - current).days
                    if diff == expire_limit:
                        print(date, "datess")
                        print(data.employee_id.name,'employeee name')
                        responsible = data.hr_responsible_id
                        for user in responsible:
                            print(user.login,"To Email")
                            print(user.name,"mail person")
                            user_email = user.login
                            list = {
                                'contract_name': data.name,
                                'name': data.employee_id.name,
                                'end_date': date,
                                'hr':user_email,
                                'days':diff
                            }
                            print(list)
                        template = self.env.ref('employee_contract_email.email_template_expiry_contract').id
                        self.env['mail.template'].browse(template).with_context(list).send_mail(self.id,force_send=True)
