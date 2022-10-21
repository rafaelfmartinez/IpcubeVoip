from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wsServer = fields.Char("WebSocket", help="The URL of your WebSocket",
                           default='wss://voip.ipcube.net:8069/ws', config_parameter='voip.wsServer')
    pbx_ip = fields.Char("PBX Server IP", help="The IP adress of your PBX Server",
                         default='voip.ipcube.net', config_parameter='voip.pbx_ip')
    mode = fields.Selection([
        ('demo', 'Demo'),
        ('prod', 'Production'),
    ], string="VoIP Environment", default='prod', config_parameter='voip.mode')
