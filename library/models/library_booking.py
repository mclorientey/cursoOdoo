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
    employee_id = fields.Many2one('hr.employee','Employee', default=_default_employee, help='Employee name')
    category_id = fields.Many2one('library.book.category','Category',help='Category to filter books')
    book_id = fields.Many2one('library.book','Book',help='The book for booking', required=True, domain="[('categ_ids','in',category_id)]")
    start_date = fields.Date('Start date', help='The start date of reservation',default=fields.Date.context_today,required=True)
    end_date = fields.Date('End date', help='The end date of reservation',required=True)
    state = fields.Selection ([('draft','Draft'),('approved','Approved'),('reserved','Reserved'),('expired','Expired'),('reject','Reject')], default="draft")
    #categ_id = fields.Integer('Categ Hidden field', compute='_calculate_categ_id')
    notes= fields.Text('Notes',required=True) 
    num_employee = fields.Integer('Employees', compute='_get_num_employees')
    num_book = fields.Integer('Books', compute='_get_num_employee_books')
    
    
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
    
    def view_all_employees(self):
        self.ensure_one()
        ids = self.env['library.booking'].read_group([ ("book_id", "=", self.book_id.id)], fields=['employee_id'], groupby=['employee_id'])
        list = []
        for id in ids:
            list.append(id['employee_id'][0])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employees',
            'view_mode': 'tree',
            'res_model': 'hr.employee',
            'domain': [('id', 'in', list)],
        }
        
    def _get_num_employees(self):
        ids = self.env['library.booking'].read_group([ ("book_id", "=", self.book_id.id)], fields=['employee_id'], groupby=['employee_id'])
        self.num_employee = len(ids) or 0
        
    
    def view_all_books_employee(self):
        self.ensure_one()
        ids = self.env['library.booking'].read_group([ ("employee_id", "=", self.employee_id.id)], fields=['book_id'], groupby=['book_id'])
        list = []
        for id in ids:
            list.append(id['book_id'][0])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employee books',
            'view_mode': 'tree',
            'res_model': 'library.book',
            'domain': [('id', 'in', list)],
        }
        
    def _get_num_employee_books(self):
        ids = self.env['library.booking'].read_group([ ("employee_id", "=", self.employee_id.id)], fields=['book_id'], groupby=['book_id'])
        self.num_book = len(ids) or 0
    