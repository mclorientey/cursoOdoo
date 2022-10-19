# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _


class libraryBook(models.Model):
    """ Modelo para definir los libros """
    _name = "library.book"
    _description = "Book"
    _order = "name desc"
    
    name = fields.Char('Nombre')
    