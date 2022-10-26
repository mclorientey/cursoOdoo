# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

def migrate(cr, version):
    value = 'Notas insertadas por la migración'
    cr.execute('UPDATE library_booking SET notes=%s where notes is null',[value])
