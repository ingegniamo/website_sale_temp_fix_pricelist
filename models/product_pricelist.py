# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from odoo.addons.website.models import ir_http


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"
    website_id=fields.Many2one('website')