# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import datetime


class libraryBook(models.Model):
    """ Modelo para definir los libros """
    _name = "library.book"
    _description = "Book"
    _order = "title desc"
    
    name = fields.Char('Name',compute='_calculate_name', help='Computed field with title and author')
    title = fields.Char('Title', required=True, help='Title of the book')
    author = fields.Char('Author', help='Person who wrote the book')
    year = fields.Selection (selection='_calculate_years', required=True, help='Year of creation since 2016 to now')
    synopsis = fields.Html('Synopsis', help='You can compose a text with the synopsis of the book')
    pages = fields.Integer('Number of pages', help='Number of pages of the book')
    editorial = fields.Char('Editorial', help='Editorial of the book')
    
    categ_ids = fields.Many2many(
        comodel_name="library.book.category",
        relation="library_book_category_rel",
        column1="book_id",
        column2="categ_id",
        string="Categories", help='All teh categories of the book'
    )
    book = fields.Binary('Book File', required=True, help='File with the book')
    reviews_id = fields.One2many('library.review','book_id','Reviews from book')
    num_booking = fields.Integer('Bookings', compute='_calculate_num_of_bookigs')
    
    @api.depends('title','author')
    def _calculate_name(self):
        for record in self:
            value = ''
            if record.title:
                value += record.title
            value +=','
            if record.author:
                value += record.author
            record.name = value
    
    def _calculate_years(self):
        today = datetime.date.today()
        year = today.year + 1
        array_years = []
        for it_year in range(2016, year):
            array_years.append((str(it_year),str(it_year)))
            #print (array_years)
        return array_years
    
    @api.constrains('title','year')
    def _check_title_year(self):
        if self.title and self.year:
            num_books = self.env['library.book'].search_count([('title','=',self.title),('year','=', self.year),('id','!=',self.id)])
            if num_books > 0:
                raise ValidationError(_("You can't create a book with this title and year"))
            
    def view_all_book_bookings(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bookings',
            'view_mode': 'tree',
            'res_model': 'library.booking',
            'domain': [('book_id', '=', self.id)],
        }
    
    def _calculate_num_of_bookigs(self):
        num = 0
        bookings = self.env['library.booking'].search_count([('book_id','=',self.id)])
        if bookings > 0:
            num = bookings
        self.num_booking = num