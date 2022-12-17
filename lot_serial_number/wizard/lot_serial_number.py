from odoo import models, fields, api, _
import xlrd
import base64

from odoo.exceptions import UserError


class TestModelWizard(models.TransientModel):
    _name = 'import.wizard.model'
    _description = 'Lot Serial number Wizard'

    name = fields.Binary(string="Select file")

    def action_import(self):
        try:
            book = xlrd.open_workbook(file_contents=(base64.decodebytes(self.name)))
        except xlrd.biffh.XLRDError:
            raise UserError('Only excel files are supported.')
        for sheet in book.sheets():
            for row in range(sheet.nrows):
                if row >= 1:
                    row_values = sheet.row_values(row)
                    # print(row_values)
                    self.env['stock.production.lot'].sudo().create({
                        'name': int(row_values[0]),
                        'ref': row_values[2],
                        'product_id': int(row_values[3]),
                        'create_date': row_values[4],
                        'company_id': int(row_values[5]),

                    })

        active_id = self.env.context.get('active_id')
        self.env['stock.production.lot'].browse(active_id).message_post(body="Successfully Imported")

