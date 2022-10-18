# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _


class libraryTestModel(models.Model):
    """ Modelo con todos los campos del sistema para ver el funcionamiento de cada uno """
    _name = "library.test.model"
    _description = "Ejemplo de campos"
    _order = "f_char desc"
    
    f_boolean = fields.Boolean('Field Booleano')
    name = fields.Char('Field Short Text')
    f_text = fields.Text('Field Text')
    f_html = fields.Html('Field WYSIWYG')
    f_integer = fields.Integer('Field Integer')
    f_float = fields.Float('Field Float')
    f_date = fields.Date('Field Date')
    f_datetime = fields.Datetime('Field Datetime')
    f_binary = fields.Binary('Field Binary')
    f_selection = fields.Selection ([('1','Primer valor'),('2','Segundo valor'),('3','Tercer valor'),('4','Cuarto valor'),('5','Quinto valor')])
    f_combo = fields.Many2one('Field Many2one', 'hr.employee')
    f_tabla = fields.One2many('library.test.model.dos','f_many2one','Field One2many')