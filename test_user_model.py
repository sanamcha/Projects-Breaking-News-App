"""User model tests."""


import os
from unittest import TestCase

from models import db, User


os.environ['DATABASE_URL'] = "postgresql:///breaking_news_app_test"


from app import app

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()

        u1 = User.register("test1", "password")
        uid1 = 1234
        u1.id = uid1

        u2 = User.register("test2", "password")
        uid2 = 3456
        u2.id = uid2

        db.session.commit()

        u1 = User.query.get(uid1)
        u2 = User.query.get(uid2)

        self.u1 = u1
        self.uid1 = uid1

        self.u2 = u2
        self.uid2 = uid2

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
   

    def test_user_model(self):
        """model work"""

        u = User(
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()


   
        

 