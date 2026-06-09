#-*- coding: utf-8 -*-

from odoo import models, fields, api


class veterinarian(models.Model):
    _name = 'vet_clinic.veterinarian'
    _description = 'Veterinario'

    name = fields.Char("Nombre ",size=64, required=True)
    email = fields.Char("Correo electrónico", required=True)
    phone = fields.Char("Telefono ",size=64)
    license_number = fields.Char("Licencia ", required=True)
    
    specialty = fields.Selection([('traumatologia','Traumatología'), 
                             ('general', 'General'),('cirugia', 'Cirugia'),('dermatologia','Dermatología')],
                             string='Especialidad', required=True)
    photo = fields.Binary('Fotografia')
    
    num_appointments = fields.Integer('Número de citas', compute='calcular_num_citas')

    status = fields.Selection([('activo','En activo'), 
                             ('baja', 'Baja'),('vacaciones', 'Vacaciones')], 
                             string='Estado', required=True,default='activo', readonly=True)
    
    appointment_ids = fields.One2many(
        string='Citas',
        comodel_name ='vet_clinic.appointment',
        inverse_name='veterinarian_id',
    )
    
    @api.depends('appointment_ids')
    def calcular_num_citas(self):
        for record in self:
            record.num_appointments = len(record.appointment_ids)

    # una sql para que el email del veterinario y su licencia sean unicas:
    _sql_constraints = [('license_number_unique','UNIQUE (license_number)','El numero de licencia ya existe para otro usuario.'),
                        ('email_unique','UNIQUE (email)','El correo electrónico debe ser único.')]
    
    # i) aqui los botones que cambian el estado

    def btn_submit_to_activo(self):
          self.write({'status':'activo'})
    def btn_submit_to_baja(self):
          self.write({'status':'baja'})
    def btn_submit_to_vacaciones(self):
          self.write({'status':'vacaciones'})

    @api.constrains('appointment_ids')
    def check_status_appointment(self):
         if self.status != 'activo':
              raise models.ValidationError('No se pueden agregar citas si el estado no es activo')
