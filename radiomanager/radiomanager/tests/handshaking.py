from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from . import AppTestCase
from .. import create_app
from ..models.device import Device


def make_public_key():
    key = ec.generate_private_key(ec.SECP256K1, default_backend())
    data = key.public_key() \
        .public_bytes(encoding=Encoding.PEM,
                      format=PublicFormat.SubjectPublicKeyInfo)
    return data


class TestPing(AppTestCase):
    def test_get_ping(self):
        response = self.client.get("/api/ping")
        self.assert200(response)

    def test_post_ping(self):
        response = self.client.post("/api/ping", data={"data": "ping"})
        self.assert200(response)
        self.assertEqual(response.json, "pong")

    def test_post_pong(self):
        response = self.client.post("/api/ping", data={"data": "pong"})
        self.assert200(response)
        self.assertEqual(response.json, "ping")

    def test_post_empty(self):
        response = self.client.post("/api/ping", data={})
        self.assert400(response)


class TestProvision(AppTestCase):
    VALID_KEY = make_public_key()

    def test_all_valid(self):
        response = self.client.post("/api/provision", data={
            "public_key": self.VALID_KEY,
            "name": "foo bar"})
        self.assert200(response)
        record = Device.query.first()
        assert record.name == b"foo bar"

    def test_invalid_name(self):
        response = self.client.post("/api/provision", data={
            "public_key": self.VALID_KEY,
            "name": "foo!bar"})
        self.assert400(response)

    def test_invalid_key(self):
        response = self.client.post("/api/provision", data={
            "public_key": "This isn't a key",
            "name": "foo bar"})
        self.assert400(response)
