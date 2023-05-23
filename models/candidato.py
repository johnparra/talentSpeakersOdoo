from odoo import models, fields

class Candidato(models.Model):
    _name = 'uniacme.candidato'
    _description = 'Candidato para votaciones'
    _inherit = 'res.partner'

    es_candidato = fields.Boolean(string='¿Es Candidato?')
    name = fields.Char(string='Nombre')
    identification = fields.Char(string='Número de identificación', required=True)

    @api.constrains('identification')
    def _check_identification_uniqueness(self):
        for record in self:
            if record.identification:
                existing_record = self.env['uniacme.candidato'].search([
                    ('identification', '=', record.identification),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing_record:
                    raise ValidationError('La identificación debe ser única.')