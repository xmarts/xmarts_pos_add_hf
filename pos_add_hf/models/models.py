# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import base64
import json
import logging

_logger = logging.getLogger(__name__)

class pos_order(models.Model):
    _inherit = "pos.order"
    
    ean13 = fields.Char('Ean13')
    
    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(pos_order, self)._order_fields(ui_order)
        
        if ui_order.get('ean13', False):
            order_fields.update({
                'ean13': ui_order['ean13']
            })
            
        return order_fields

class pos_config_adds(models.Model):
    _inherit = "pos.config"

    direccion_ptv = fields.Char(string="Dirección de PTV")
    rfc_ptv = fields.Char(string="RFC de PTV")
    encargado_ptv = fields.Char(string="Encargado de PTV")
    logo_ptv = fields.Binary(string="Logo de encabezado")
    telefono_ptv = fields.Char(string="Teléfono de PTV")
    text_footer = fields.Text(string="Texto del pie de pagina")