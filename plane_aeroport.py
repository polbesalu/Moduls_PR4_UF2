from odoo import models, fields

class plane(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer()
    nom = fields.Char()
    imatge = fields.Binary(string="Imatge")
    ciutat = fields.Char()
    pais = fields.Char()
    latitud = fields.Integer()
    longitud = fields.Integer()
    codi_vol_anada = fields.One2many('plane.vol')
    codi_vol_tornada = fields.One2many('plane.vol')