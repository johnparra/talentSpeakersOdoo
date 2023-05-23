from odoo import models, fields

class Voto(models.Model):
    _name = 'uniacme.voto'
    _description = 'Voto en una votación'

    candidato_id = fields.Many2one('uniacme.candidato', string='Candidato')
    votacion_id = fields.Many2one('uniacme.votacion', string='Votación')
    foto_candidato = fields.Binary(string='Foto del candidato')

    _sql_constraints = [
        ('unique_estudiante_votacion', 'unique(estudiante_id, votacion_id)', 'Cada estudiante solo puede votar una vez en una votación.')
    ]
