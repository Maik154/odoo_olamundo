from odoo import models, fields, api


class olamundo(models.Model):
    _name = "odoo_olamundo.olamundo"
    _description = "exemplo olamundo"
    name = fields.char(string="Ola Mundo")
