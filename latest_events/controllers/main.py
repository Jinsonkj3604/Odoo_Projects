from odoo import http
from odoo.http import request
import json


class Events(http.Controller):
    @http.route(["/events/snippet"], type="json", auth="public")
    def event_latest(self):
        event = request.env['event.event'].sudo().search([], limit=6)
        event_list = []
        event_group = []
        for values in event:
            data = json.loads(values["cover_properties"])
            img = data['background-image'][5:-2]
            data = {
                'name' : values.name,
                'venue' : values.address_id.name,
                'date_begin':values.date_begin,
                'date_end':values.date_end,
                'url': values.website_url,
                'img': img
            }
            event_list.append(data)

            if len(event_list) >= 4:
                event_group.append(event_list)
                event_list = []

        if event_group:
            group = event_group[0]

        print("first",event_list)
        print('group', group)

        latest = {
            'value': event_group,
            'slider': group
        }

        print("second",latest)
        responce = http.Response(template="latest_events.basic_snippet", qcontext=latest)
        return responce.render()
