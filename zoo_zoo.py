from odoo import models, fields

class zoo(models.Model):
    _name = 'zoo.zoo'
    id = fields.Integer()
    grandaria = fields.Integer()
    nom = fields.Char()
    pais = fields.Char()
    ciutat = fields.Char()
    zoo_id = fields.One2many('zoo.animal')