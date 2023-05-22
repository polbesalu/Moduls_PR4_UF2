from odoo import models, fields

class plane(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer()
    dataSortida = fields.Date()
    dataArribada = fields.Date()
    passatgers = fields.Integer()
    codi_pilot = fields.Many2one('plane.pilot')
    codi_avio = fields.Many2one('plane.avio')
    codi_aeroport = fields.Many2one('plane.aeroport')