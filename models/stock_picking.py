# models/stock_picking.py

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    scanned_barcode = fields.Char(string='Scanned Barcode')

    @api.onchange('scanned_barcode')
    def _check_scanned_barcode(self):
        for line in self.move_line_ids:
            if line.product_id.barcode == self.scanned_barcode:
                line.qty_done += 1
                self.scanned_barcode = False
                return {
                    'warning': {
                        'title': "Producto Valido",
                        'message': "El Producto Escaneado Corresponde al del Pedido",
                    }
                }
        return {
            'warning': {
                'title': "Producto no Encontrado",
                'message': "El Producto Escaneado no Corresponde a ninguno en la linea de Pedido",
            }
        }
