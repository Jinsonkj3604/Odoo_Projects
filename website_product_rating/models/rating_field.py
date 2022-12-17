from odoo import models,fields,api

class RatingSort(models.Model):
    _inherit = "product.template"

    rating = fields.Char(compute="_compute_avg_rating", store=True)


    @api.depends('rating_avg')
    def _compute_avg_rating(self):

        for rec in self:
            rec.rating = rec.rating_avg
