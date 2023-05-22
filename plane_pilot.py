from odoo import models, fields

class plane(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer()
    nom = fields.Char()
    cognoms = fields.Char()
    nif = fields.Char()
    telf = fields.Char()
    email = fields.Char()
    codi_vol = fields.One2many('plane.vol')
