# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DemandeAchat(models.Model):
    _name = 'demande.achat'
    _description = 'Demande Achat'

    name = fields.Char(string='Name', default = lambda self : ('DA'),readonly=1)
    demandeur = fields.Many2one('res.partner',string='Demandeur', required=True)
    date_dmd = fields.Date(string='Date de la demande', required=True)
    etat_dmd = fields.Selection([
        ('draft','Draft'),
        ('open','Open'),
        ('confirmed','Confirmed'),
        ('done','Done')],string='Etat de la demande', default='draft'
        
    )
    approbateur = fields.Many2one('hr.employee',string='Approbateur',required=True)
    demande_line = fields.One2many('demande.achat.line','demande_id', string='Liste des produits')


    @api.model
    def create(self,vals):
        if vals.get('name',('DA')) == ('DA') :
            vals['name'] = self.env['ir.sequence'].next_by_code('demande.achat') or ('DA')
            delta = super(DemandeAchat,self).create(vals)
            return delta

 

    
class DemandeAchatLine(models.Model):
    _name = 'demande.achat.line'
    _description = 'Demande Achat Line'
    
    product_id = fields.Many2one('product.product', string='Produit')
    product_qty = fields.Integer(string="Quantité")
    product_unite = fields.Many2one('product.category', string='Unité de mesure')

    demande_id = fields.Many2one('demande.achat',string='demande id')