from odoo import models, fields, _
import json
import io
import xlsxwriter

class PackageReportWizard(models.TransientModel):
    _name = 'pdf.report.wizard'
    _description = 'Package Report Wizard'

    person_id = fields.Many2one('res.users', string="Sales Person")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string='To Date')

    def action_pdf_print(self):
        sql_query = """ select sale_package_bundle.seq_no as Bundle,sale_package_model.name as pack,product_template.name as product,sale_package_model.width,sale_package_model.height,sale_package_model.m_weight as Weight
                       from sale_package_model inner join sale_package_bundle on sale_package_model.id = sale_package_bundle.id
                       inner join sale_package_bundle_page on sale_package_model.id  = sale_package_bundle_page.id 
					   inner join product_template on sale_package_bundle_page.product_id = product_template.id"""
        if self.from_date:
            f_date= """ where sale_package_bundle.date >= '%s' """ %self.from_date
            sql_query += f_date
        if self.to_date:
            new= """ and sale_package_bundle.ex_date <= '%s' """ %self.to_date
            sql_query += new

        if self.person_id:
            person = """ and sale_package_bundle.person_id = '%s' """%self.person_id.id
            sql_query += person

        self.env.cr.execute(sql_query)
        val = self.env.cr.dictfetchall()

        data = {
            'person_id': self.person_id.name,
            'to_date': self.to_date,
            'from_date': self.from_date,
            'new': val
        }
        print(data)
        return self.env.ref('so_package.action_report_package_order').report_action(self, data=data)


    def action_excel_print(self):
        sql_query = """ select sale_package_bundle.seq_no as Bundle,sale_package_model.name as pack,product_template.name as product,sale_package_bundle_page.quantity,sale_package_model.width,sale_package_model.height,sale_package_model.m_weight as Weight
                               from sale_package_model inner join sale_package_bundle on sale_package_model.id = sale_package_bundle.id
                               inner join sale_package_bundle_page on sale_package_model.id  = sale_package_bundle_page.id 
        					   inner join product_template on sale_package_bundle_page.product_id = product_template.id"""
        if self.from_date:
            f_date = """ where sale_package_bundle.date >= '%s' """ % self.from_date
            sql_query += f_date
        if self.to_date:
            new = """ and sale_package_bundle.ex_date <= '%s' """ % self.to_date
            sql_query += new

        if self.person_id:
            person = """ and sale_package_bundle.person_id = '%s' """ % self.person_id.id
            sql_query += person

        self.env.cr.execute(sql_query)
        val = self.env.cr.dictfetchall()
        print(val)

        data = {
            'person_id': self.person_id.name,
            'to_date': self.to_date,
            'from_date': self.from_date,
            'new': val
        }
        return{
            'type': 'ir.actions.report',
            'data': {'model': 'pdf.report.wizard',
                'options': json.dumps(data, default=fields.date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report Name',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        tiltle = workbook.add_format({'font_size':'12px','align':'center','bold':True})
        cell_format = workbook.add_format({'font_size': '11px','bold':True})
        head = workbook.add_format({'align': 'center', 'bold': True,'font_size':'20px'})
        txt = workbook.add_format({'font_size': '10px','align':'center'})
        sheet.merge_range('B2:I3', 'Package Bundle Report', head)
        if data.get('from_date'):
            sheet.write('B5', 'From:', cell_format)
            sheet.merge_range('C5:D5', data['from_date'],txt)
        if data.get('to_date'):
            sheet.write('B7', 'To:', cell_format)
            sheet.merge_range('C7:D7', data['to_date'],txt)
        if data.get('person_id'):
            sheet.write('B9', 'sales person:', cell_format)
            sheet.merge_range('C9:D9', data['person_id'], txt)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 15)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 15)
        sheet.set_column('G:G', 15)
        sheet.set_column('H:H', 15)
        sheet.set_column('I:I', 15)
        row =11
        col = 1
        sheet.write(row,col, 'sl_no', tiltle)
        sheet.write(row,col+1, 'Bundle', tiltle)
        sheet.write(row,col+2, 'Pack', tiltle)
        sheet.write(row,col+3, 'Product', tiltle)
        sheet.write(row,col+4, 'Quantity', tiltle)
        sheet.write(row,col+5, 'Width' , tiltle)
        sheet.write(row,col+6, 'Height', tiltle)
        sheet.write(row,col+7, 'Weight', tiltle)

        row =12
        col = 1
        sl_no = 0
        dict = data.get('new')
        for i in dict:
            row = row + 1
            sl_no = sl_no + 1
            sheet.write(row, col, sl_no)
            sheet.write(row, col+1, i.get('bundle'),txt)
            sheet.write(row, col+2, i.get('pack'),txt)
            sheet.write(row, col+3, i.get('product'),txt)
            sheet.write(row, col+4, i.get('quantity'),txt)
            sheet.write(row, col+5, i.get('width'),txt)
            sheet.write(row, col+6, i.get('height'),txt)
            sheet.write(row, col+7, i.get('weight'),txt)

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()


    def action_close(self):
        pass
