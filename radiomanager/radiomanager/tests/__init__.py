from flask_testing import TestCase
from .. import create_app, TESTING_CONFIG, FlaskExtensions


class AppTestCase(TestCase):
    def create_app(self):
        return create_app(TESTING_CONFIG)

    def setUp(self):
        with self.app.app_context():
            FlaskExtensions.db.create_all()

    def tearDown(self):
        super().tearDown()
        with self.app.app_context():
            FlaskExtensions.db.session.remove()
            FlaskExtensions.db.drop_all()
        FlaskExtensions.reset()
