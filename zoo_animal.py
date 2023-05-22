from odoo import models, fields

class animal(models.Model):
    _name = 'zoo.animal'
    id = fields.Integer()
    sexe = fields.Char()
    dataNaix = fields.Date()
    paisOrigen = fields.Char()
    continentOrigen = fields.Char()
    especie_id = fields.Many2one('zoo.especie')
    zoo_id = fields.Many2one('zoo.especie')
