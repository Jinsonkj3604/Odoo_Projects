from odoo import fields, models, api,_


class ImportLotAndSerial(models.Model):
    _inherit = "stock.production.lot"
    _description = "import lot and serial number"

    def import_data_action(self):

        return {
            'name': _('Lot and Serial Number'),
            'type': 'ir.actions.act_window',
            'res_model': 'import.wizard.model',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new'

        }
