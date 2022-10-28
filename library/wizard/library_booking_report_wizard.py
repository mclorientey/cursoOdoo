# -*- coding: utf-8 -*-
#
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.
#

from odoo import api, fields, models, _, exceptions

class LibraryBookingkReportWizard(models.TransientModel):
    _name = "library.booking.report.wizard"
    _description = "Wizard de ejemplo lanzar report"
    
    start_date = fields.Date('Start date', help='The start date of reservation',required=True)
       
       
    def launchReport(self):
        bookings = self.env['library.booking'].search([('start_date','>=', self.start_date)])
        return self.env.ref('library.library_booking_report_action').report_action(bookings, None)
    