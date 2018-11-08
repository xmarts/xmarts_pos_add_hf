# -*- coding: utf-8 -*-
from openerp import models, fields, api

class pos_config_adds(models.Model):
	_inherit = "pos.config"

	direccion_ptv = fields.Char(string="Dirección de PTV")
	rfc_ptv = fields.Char(string="RFC de PTV")
	encargado_ptv = fields.Char(string="Encargado de PTV")
	logo_ptv = fields.Binary(string="Logo de encabezado")
	telefono_ptv = fields.Char(string="Teléfono de PTV")
	text_footer = fields.Text(string="Texto del pie de pagina")