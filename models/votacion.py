from odoo import models, fields

class Votacion(models.Model):
    _name = 'uniacme.votacion'
    _description = 'Proceso de votación'

    name = fields.Char(string='Descripción')
    fecha_inicio = fields.Datetime(string='Fecha de inicio')
    fecha_fin = fields.Datetime(string='Fecha de fin')
    candidatos_ids = fields.Many2many('uniacme.candidato', string='Candidatos')
    votos_por_candidato = fields.One2many('uniacme.voto', 'votacion_id', string='Votos por candidato')
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_proceso', 'En proceso'),
        ('cerrada', 'Cerrada')
    ], default='borrador', string='Estado')