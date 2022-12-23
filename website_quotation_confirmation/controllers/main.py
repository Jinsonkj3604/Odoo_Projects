import json

from odoo import http
from odoo.http import content_disposition, request

class WebsiteForm(http.Controller):

    @http.route(['/checkbox/active/order'], type='json', auth='public', website=True)
    def sale_order_confirm(self,**kw):
        print(kw, "dictionary")
        for val in kw:
            print(kw[val],"value list")
            list = kw[val]
            for i in range(len(list)):
                # print(list[i], "value")
                id = list[i]
                print(type(id))
                id = int(id)
                print(id,"each id")
                order= request.env['sale.order'].browse(id).action_confirm()

