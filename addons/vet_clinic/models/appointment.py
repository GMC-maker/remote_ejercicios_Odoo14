# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class appointment(models.Model):
    _name = 'vet_clinic.appointment'
    _description = 'Citas'

    name = fields.Datetime(
        string='Fecha de la proxima cita',
        default=fields.Datetime.now,
        required=True
    )
    pet_name = fields.Char("Nombre de su mascota: ",size=64, required=True)
    owner_phone = fields.Char("Telefono de contacto: ",size=64)
    reason = fields.Text("Razón de la cita ")
    
    veterinarian_id = fields.Many2one(
        string='Veterinario(a)',
        comodel_name='vet_clinic.veterinarian',
        ondelete='restrict', required=True  #esta bien solo si no quiero borrar un vet con citas programadas
    )
    
    ##para que se vea bonito el campo en el calendario, sino solo sale la fecha:
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = record.pet_name or 'Cita'
    #         result.append((record.id, name))
    #     return result
    
    def name_get(self):
        result = []
        for record in self:
            name = record.pet_name or 'Cita'
            if record.name:
                name = '%s - %s' % (name, record.name.strftime('%H:%M'))
            result.append((record.id, name))
        return result
    
    #j) para validar o crear una restriccion, no se pueden agregar citas a un vet que no este activo.
    @api.constrains('veterinarian_id')
    def _check_veterinarian_active(self):
        for record in self:
            if record.veterinarian_id and record.veterinarian_id.status != 'activo':
                raise ValidationError(
                    'No se pueden agregar citas a un veterinario que no este en activo.'
                )
            
    def unlink(self):
        for record in self:
            if record.veterinarian_id and record.veterinarian_id.status != 'activo':
                raise ValidationError(
                    'No se pueden eliminar citas de un veterinario que no este en activo.'
                )
        return super().unlink()