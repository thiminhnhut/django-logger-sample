from marshmallow import Schema, fields, EXCLUDE, post_load


class Sensor:
    def __init__(self, timestamp, temp, humi):
        self.timestamp = timestamp
        self.temp = temp
        self.humi = humi

    def __str__(self):
        return f"Sensor(timestamp={self.timestamp}, temp={self.temp}, humi={self.humi})"


class SensorSchema(Schema):
    timestamp = fields.Integer(required=True)
    temp = fields.Float(required=True)
    humi = fields.Float(required=True)

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_student(self, data, **kwargs):
        return Sensor(**data)
