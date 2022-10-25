# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import datetime


class libraryReview(models.Model):
    """ Modelo para definir las reseñas """
    _name = "library.review"
    _description = "Review"
    _order = "rating desc"
    
    def _default_employee(self):
        return self.env.user.employee_ids[0].id
    
    name = fields.Char('Name',compute='_calculate_name', help='Computed field with Book and Employee', store=True)
    employee_id = fields.Many2one('hr.employee','Employee', default=_default_employee, help='Employee name')
    book_id = fields.Many2one('library.book','Book',help='The book for booking', required=True)
    text = fields.Html('Review', help='You can compose a text with the review of the book')
    rating = fields.Selection([('0','Not reviewed'),('1','Very Bad'),('2','Bad'),('3','Normal'),('4','Good'),('5','Very Good')])
    
    @api.depends('employee_id','book_id')
    def _calculate_name(self):
        for record in self:
            value = ''
            if record.employee_id and record.employee_id.name:
                value += record.employee_id.name
            value +=','
            if record.book_id and record.book_id.name:
                value += record.book_id.name
            record.name = value