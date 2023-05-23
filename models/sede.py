from odoo import models, fields


class Sede(models.Model):
    _name = 'uniacme.sede'
    _description = 'Sede de la universidad'

    name = fields.Char(string='Nombre de la sede')
