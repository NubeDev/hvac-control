from flask_restful import Api

from src import app
from src.resources.ping import Ping
from src.resources.schedule.schedule_name import ScheduleName
from src.resources.schedule.schedule_plural import SchedulePlural
from src.resources.schedule.schedule_singular import ScheduleSingular
# from src.resources.serial_driver.serial import SerialDriver

api_prefix = '/api'
api = Api(app)

lora_api_prefix = '{}/control'.format(api_prefix)
# api.add_resource(SerialDriver, '{}/networks'.format(lora_api_prefix))
api.add_resource(SchedulePlural, '{}/schedules'.format(lora_api_prefix))
api.add_resource(ScheduleSingular, '{}/schedules/uuid/<string:uuid>'.format(lora_api_prefix))
api.add_resource(ScheduleName, '{}/schedules/name/<string:name>'.format(lora_api_prefix))

system_api_prefix = '{}/system'.format(api_prefix)
api.add_resource(Ping, system_api_prefix, '{}/ping'.format(system_api_prefix))
