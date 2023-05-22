from odoo import models, fields

class plane(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer()
    imatge = fields.Binary(string="Imatge")
    marca = fields.Integer()
    model = fields.Char()
    maxVel = fields.Integer()
    codi_vol = fields.One2many('plane.vol')
