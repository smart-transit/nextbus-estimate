
from collections import namedtuple
from pprint import pprint
from marshmallow import Schema, fields, post_load


class User(namedtuple('User', [
    'name', 'email', 'created_at'])):
    """
    """

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_obj(self, data):
        return User(**data)



user_data = {
    'created_at': '2014-08-11T05:26:03.869245',
    'email': u'ken@yahoo.com',
    'name': u'Ken'
}
schema = UserSchema()
#result = schema.dump(user_data)
#pprint(result)
#pprint(result.data['name'])

user_data_str = """
{
	"created_at": "2014-08-11T05:26:03.869245",
	"email": "ken@yahoo.com",
	"name": "Ken"
}
"""

result = schema.load(user_data, many=False)
pprint(result)
pprint(result.name)

