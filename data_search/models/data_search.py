from odoo import models, fields

class DataSearchFiled(models.Model):
    _name = "data.search.model"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Data search in models"
    _rec_name = 'search_data'

    search_data = fields.Char(required=True)
    field_name = fields.Char()
    content_ids = fields.One2many('data.search.page', 'data_search_id')

    def search_action_confirm(self):

        self.write({'content_ids': [(5, 0, 0)]})


        # selected model list
        models = ['res.partner', 'sale.order', 'product.product', 'product.template', 'sale.order.line','res.country']
        for rec in models:
            # To get the fields model in list  in ir.model
            fields = self.env['ir.model'].search([('model', '=', rec)]).field_id
            # search the records in model
            for rec_set in self.env[rec].search([]):
                print(rec_set,"records of the model")
                for field in fields:
                    print("field names",field.name)
                    print(" records of the each field", rec_set[field.name])
                    try:
                        if self.search_data.lower() in rec_set[field.name].lower():
                            self.write({
                                        'content_ids':[(0,0,{
                                                'value':rec_set[field.name],
                                                'model_name': rec,
                                                'field_name': field.name
                                                })]
                                            })
                    except:
                        pass



    class ResultDataSearch(models.Model):
        _name = 'data.search.page'

        value = fields.Char()
        model_name = fields.Char()
        data_search_id = fields.Many2one('data.search.model')
        field_name = fields.Char()
