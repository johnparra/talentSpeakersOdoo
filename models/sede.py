from odoo import models, fields


class Sede(models.Model):
    _name = 'uniacme.sede'
    _description = 'Sede de la universidad'

    name = fields.Char(string='Nombre de la sede')
    zona_horaria = fields.Selection([
        ('Europe/Brussels', 'Bélgica'),
        ('America/Bogota', 'Colombia'),
        ('America/Caracas', 'Venezuela'),
        ('America/Argentina/Buenos_Aires', 'Argentina')
    ], string='Zona horaria')