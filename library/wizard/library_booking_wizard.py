# -*- coding: utf-8 -*-
#
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
#

from odoo import api, fields, models, _, exceptions

class LibraryBookingkWizard(models.TransientModel):
    _name = "library.booking.wizard"
    _description = "Wizard de ejemplo"
    
    text = fields.Char('Add notes', help='Text to add in the notes')
    choose_state = fields.Selection ([('draft',_('Draft')),('approved',_('Approved')),('reserved',_('Reserved')),('expired',_('Expired')),('reject',_('Reject'))], default="draft")
       
       
    def addTextToNotes(self):
        bookings = self.env['library.booking'].search([('state','=',self.choose_state)])
        bookings.write({'notes':self.text})
    