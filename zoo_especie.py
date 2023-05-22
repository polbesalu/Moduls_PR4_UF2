from odoo import models, fields

class especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Integer()
    familia = fields.Char()
    perill = fields.Char()
    nomCientific = fields.Char()
    nomVulgar = fields.Char()
    animal_id = fields.One2many('zoo.animal')