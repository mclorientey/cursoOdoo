# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    book_id = fields.Many2one('library.book',help="Merchandasing asociation")