# Copyright 2024 Odoo Community Association (OCA)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_linkedin = fields.Char(string="LinkedIn Profile URL")
    social_twitter = fields.Char(string="Twitter/X Profile URL")
    social_github = fields.Char(string="GitHub Profile URL")
    social_facebook = fields.Char(string="Facebook Profile URL")
    social_instagram = fields.Char(string="Instagram Profile URL")
    social_youtube = fields.Char(string="YouTube Channel URL")
