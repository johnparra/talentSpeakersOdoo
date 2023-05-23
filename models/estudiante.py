from odoo import models, fields

class Estudiante(models.Model):
    _name = 'uniacme.estudiante'
    _description = 'Estudiante de la universidad'
    _inherit = 'res.partner'

    es_estudiante = fields.Boolean(string='¿Es Estudiante?')
    name = fields.Char(string='Nombre')
    identification = fields.Char(string='Número de identificación', required=True)
    carrera = fields.Char(string='Carrera')
    sede_id = fields.Many2one('uniacme.sede', string='Sede')

    @api.constrains('identification')
    def _check_identification_uniqueness(self):
        for record in self:
            if record.identification:
                existing_record = self.env['uniacme.estudiante'].search([
                    ('identification', '=', record.identification),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing_record:
                    raise ValidationError('La identificación debe ser única.')