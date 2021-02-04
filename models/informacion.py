from odoo import models, fields, api


class informacion(models.Model):
    _name = "odoo_basico.informacion"
    _description = " Tipos de datos basicos"

    name = fields.Char(string="Titulo", required=True, size=20)
    descripcion = fields.Text(string="A Descripcion")
    autorizado = fields.Boolean(string="¿Esta autorizado?", default=True)
    sexo_traducido = fields.Selection([("Hombre", "Home"),("Mujer","Muller"),("Otros","Outros")],string="Sexo")
    alto_en_cms = fields.Integer(string="Alto em cms")
    longo_en_cms = fields.Integer(string="Longo en cms")
    ancho_en_cms = fields.Integer(string="Ancho en cms")