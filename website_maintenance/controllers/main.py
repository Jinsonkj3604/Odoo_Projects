import json

from odoo import http
from odoo.http import content_disposition, request

class WebsiteForm(http.Controller):

   @http.route(['/maintenance'], type='http', auth="user", website=True)
   def maintenance(self):
       partners = request.env['res.partner'].sudo().search([])
       equipments = request.env['maintenance.equipment'].sudo().search([])
       print(equipments)
       values = {}
       values.update({
           'partners': partners,
           'equipments': equipments
       })
       return request.render("website_maintenance.online_maintenance_form", values)

   @http.route(['/maintenance/submit'], type='http', auth="user", website=True)
   def action_submit(self,**post):
       print("data", post)
       req ={
           'name': post.get('name'),
           'equipment_id': int(post.get('equipment_id')),
           'schedule_date': post.get('schedule_date'),
           'maintenance_type':post.get('maintenance_type'),
           'email_cc':post.get('email_cc')
           }
       last_id = request.env['maintenance.request'].sudo().create(req)
       print(req,"req data")
       print(last_id,"last_ids data")
       template = request.env.ref('website_maintenance.email_template_maintenance')
       print(template)
       template.sudo().send_mail(last_id.id, force_send=True)
       return request.render("website_maintenance.tmp_customer_form_success",{})

