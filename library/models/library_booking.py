# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _
from datetime import datetime, timedelta

class libraryBooking(models.Model):
    """ Modelo para definir las reservas"""
    _name = "library.booking"
    _description = "Booking books"
    _order = "start_date desc"
    
    def _default_employee(self):
        return self.env.user.employee_ids[0].id
    
    name = fields.Char('Name',compute='_calculate_name', help='Computed field with employee and book name')
    employee_id = fields.Many2one('hr.employee','Employee', default=_default_employee, help='Computed field with title and author')
    category_id = fields.Many2one('library.book.category','Category',help='Category to filter books')
    book_id = fields.Many2one('library.book','Book',help='The book for booking', required=True, domain="[('categ_ids','in',category_id)]")
    start_date = fields.Date('Start date', help='The start date of reservation',default=fields.Date.context_today,required=True)
    end_date = fields.Date('End date', help='The end date of reservation',required=True)
    state = fields.Selection ([('draft','Draft'),('approved','Approved'),('reserved','Reserved'),('expired','Expired'),('reject','Reject')], default="draft")
    #categ_id = fields.Integer('Categ Hidden field', compute='_calculate_categ_id')
    
    
    @api.depends('book_id','employee_id')
    def _calculate_name(self):
        for record in self:
            value = ''
            if record.employee_id and record.employee_id.name:
                value += record.employee_id.name
            value +=' - '
            if record.book_id and record.book_id.name:
                value += record.book_id.name
            record.name = value
   
   
   
    ''' DEPRECATED
    @api.onchange('category_id')
    def domain_book(self):
        if self.category_id:
            return {'domain': {'book_id': [('categ_ids', 'in', self.category_id.id)]}}
    
            
    @api.depends('category_id')
    def _calculate_categ_id(self):
        for record in self:
            if record.category_id:
                record.categ_id =record.category_id.id
            else:
                record.categ_id = 0
    '''  
    
    @api.model                
    def create(self, vals):
        if 'start_date' in vals:
            vals['end_date'] = self._calculate_end_date(vals['start_date'])
        return super(libraryBooking, self).create(vals)
    
    def write(self, vals):
        if 'start_date' in vals:
            vals['end_date'] = self._calculate_end_date(vals['start_date'])
        return super(libraryBooking, self).write(vals)
    
    def _calculate_end_date(self,start_date):
        fecha = fields.Date.from_string(start_date)
        fecha_fin = fecha + timedelta(days=3)  
        return fecha_fin.strftime("%Y-%m-%d")