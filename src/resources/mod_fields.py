from flask_restful import fields


schedule_fields = {
    'uuid': fields.String,
    'name': fields.String,
    'description': fields.String,
    'enable': fields.Boolean,

}

