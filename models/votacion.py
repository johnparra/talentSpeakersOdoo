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
    sede_id = fields.Many2one('uniacme.sede', string='Sede')
    votos_ids = fields.One2many('uniacme.voto', 'votacion_id', string='Votos')

    def iniciar_votacion(self):
        self.write({'estado': 'en_proceso'})

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fecha_hora(self):
        for votacion in self:
            if votacion.fecha_inicio and votacion.fecha_fin:
                fecha_inicio = fields.Datetime.from_string(votacion.fecha_inicio)
                fecha_fin = fields.Datetime.from_string(votacion.fecha_fin)
                if fecha_inicio > fecha_fin:
                    raise models.ValidationError("La fecha y hora de inicio deben ser anteriores a la fecha y hora de finalización.")

    @api.constrains('fecha_inicio', 'fecha_fin', 'sede_id')
    def _check_fecha_hora_sede(self):
        for votacion in self:
            if votacion.fecha_inicio and votacion.fecha_fin and votacion.sede_id:
                fecha_inicio = fields.Datetime.from_string(votacion.fecha_inicio)
                fecha_fin = fields.Datetime.from_string(votacion.fecha_fin)
                sede = votacion.sede_id
                if fecha_inicio and fecha_fin and sede:
                    tz_sede = timezone(sede.zona_horaria)
                    fecha_inicio_sede = fecha_inicio.astimezone(tz_sede)
                    fecha_fin_sede = fecha_fin.astimezone(tz_sede)
                    now = datetime.now(tz_sede)
                    if now < fecha_inicio_sede or now > fecha_fin_sede:
                        raise models.ValidationError("La votación no puede realizarse en este momento según la zona horaria de la sede.")