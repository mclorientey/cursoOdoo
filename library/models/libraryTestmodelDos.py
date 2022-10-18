# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2005-2006 Axelor SARL. (http://www.axelor.com)

from odoo import api, fields, models, _


class libraryTestModelDos(models.Model):
    """ Modelo con todos los campos del sistema para ver el funcionamiento de cada uno """
    _name = "library.test.model.dos"
    _description = "Ejemplo de campos"
    _order = "name desc"
    
    name = fields.Char('Field Short Text')
    f_many2one = fields.Many2one('library.test.model', string="Many2one")