# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _


class libraryBookCategory(models.Model):
    """ Modelo para definir las distintas categorías de un libro """
    _name = "library.book.category"
    _description = "Book Categories"
    _order = "name desc"
    
    name = fields.Char('Nombre')
    