# Copyright 2024 Odoo Community Association (OCA)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class TestResPartnerSocialMedia(common.TransactionCase):
    def setUp(self):
        super(TestResPartnerSocialMedia, self).setUp()
        self.partner = self.env.ref("base.partner_admin")

    def test_social_media_fields(self):
        self.partner.write(
            {
                "social_linkedin": "https://www.linkedin.com/in/testuser",
                "social_twitter": "https://twitter.com/testuser",
                "social_github": "https://github.com/testuser",
                "social_facebook": "https://www.facebook.com/testuser",
                "social_instagram": "https://www.instagram.com/testuser",
                "social_youtube": "https://www.youtube.com/c/testuser",
            }
        )
        self.assertEqual(
            self.partner.social_linkedin, "https://www.linkedin.com/in/testuser"
        )
        self.assertEqual(
            self.partner.social_twitter, "https://twitter.com/testuser"
        )
        self.assertEqual(
            self.partner.social_github, "https://github.com/testuser"
        )
        self.assertEqual(
            self.partner.social_facebook, "https://www.facebook.com/testuser"
        )
        self.assertEqual(
            self.partner.social_instagram, "https://www.instagram.com/testuser"
        )
        self.assertEqual(
            self.partner.social_youtube, "https://www.youtube.com/c/testuser"
        )

    def test_social_media_fields_empty(self):
        self.partner.write(
            {
                "social_linkedin": False,
                "social_twitter": False,
                "social_github": False,
                "social_facebook": False,
                "social_instagram": False,
                "social_youtube": False,
            }
        )
        self.assertFalse(self.partner.social_linkedin)
        self.assertFalse(self.partner.social_twitter)
        self.assertFalse(self.partner.social_github)
        self.assertFalse(self.partner.social_facebook)
        self.assertFalse(self.partner.social_instagram)
        self.assertFalse(self.partner.social_youtube)
