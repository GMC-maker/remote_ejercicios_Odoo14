# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class match_appointment(models.Model):
    _name='love_match_r.match_appointment'
    _description = 'Citas Match'
    _rec_name = 'user_from_id' #esto solo se usa si el modelo no tiene un name ya dado...

    user_from_id = fields.Many2one(
            string='user_from_id',
            comodel_name='love_match_r.match_user',
            ondelete='restrict', required=True  #campo restringido solo si no quiero borrar un usuario con citas programadas
        )

    user_to_id = fields.Many2one(
            string='user_to_id',
            comodel_name='love_match_r.match_user',
            ondelete='restrict', required=True  
        )

    scheduled_datetime = fields.Datetime(
            string='Fecha de la proxima cita',
            default=fields.Datetime.now
        )
    location = fields.Char("Location")

    status = fields.Selection([('pending','Pending'), 
                                ('confirmed', 'Confirmed'),('cancelled', 'Cancelled')], 
                                string='Status', default='pending')

    notes = fields.Text("Notes: ")


    @api.constrains('user_from_id', 'user_to_id')
    def _check_user_status(self):
        for record in self:
            if record.user_from_id.status in ['onBreak', 'banned']:
                raise ValidationError('No se puede crear la cita porque el usuario solicitante esta en descanso o bloqueado.')

            if record.user_to_id.status in ['onBreak', 'banned']:
                raise ValidationError('No se puede crear la cita porque el usuario receptor esta en descanso o bloqueado.')