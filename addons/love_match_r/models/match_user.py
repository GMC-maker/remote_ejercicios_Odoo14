#-*- coding: utf-8 -*-

from odoo import models, fields, api
#from odoo.exceptions import ValidationError

class love_match_r(models.Model):
    _name = 'love_match_r.match_user'
    _description = 'Usuario'

    
    name = fields.Char("Nombre ", required=True)
    email = fields.Char("Correo electrónico", required=True)
    age = fields.Integer("Edad")

    gender = fields.Selection([('femenino','Femenino'), 
                            ('masculino', 'Masculino'),('otro', 'Otro')],'Genero', required=True)
    
    photo = fields.Binary('Photo')
    
    biography = fields.Text('Biography')

    status = fields.Selection([('active','Active'), 
                             ('on_break', 'On Break'),('banned', 'Banned')], 
                             string='Estado', required=True,default='active', readonly=True)
    num_appointments = fields.Integer('Número de citas', compute='calcular_num_citas', store=True)
    #num_appointments sea store=True, es un campo calculado si no almacenado,
    # la vista graph te puede dar problemas o no agrupar/medir bien.


    match_ids =  fields.One2many(
        string='Match_ids',
        comodel_name ='love_match_r.match_appointment',
        inverse_name='user_from_id',
    )

    received_match_ids = fields.One2many(
        string='Received_match_ids',
        comodel_name ='love_match_r.match_appointment',
        inverse_name='user_to_id',
    )

    @api.depends('match_ids','received_match_ids')
    def calcular_num_citas(self):
        for record in self:
            record.num_appointments = len(record.match_ids) + len(record.received_match_ids)

    # i) aqui los botones que cambian el estado

    def btn_submit_to_active(self):
          self.write({'status':'active'})
    def btn_submit_to_on_break(self):
          self.write({'status':'on_break'})
    def btn_submit_to_banned(self):
          self.write({'status':'banned'})
    
    # una sql constraint para que el email sea unique:
    _sql_constraints = [
    ('unique_email', 'unique(email)', 'El email debe ser unico.')
]
    #borrar todas las citas pendientes: 
    def btn_delete_pending_appointments(self):
        for record in self:
            for cita in record.match_ids:
                if cita.status == 'pending':
                    cita.unlink()

            for cita in record.received_match_ids:
                if cita.status == 'pending':
                    cita.unlink()