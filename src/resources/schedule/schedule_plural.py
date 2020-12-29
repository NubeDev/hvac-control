import uuid
from flask_restful import marshal_with
from src.models.schedule.model_schedule import ScheduleModel
from src.resources.schedule.mod_fields import schedule_fields
from src.resources.schedule.schedule_base import ScheduleBase


class SchedulePlural(ScheduleBase):
    @marshal_with(schedule_fields)
    def get(self):
        return ScheduleModel.get_all()

    @marshal_with(schedule_fields)
    def post(self):
        uuid_ = str(uuid.uuid4())
        data = SchedulePlural.parser.parse_args()
        return self.add_schedule(uuid_, data)

    def delete(self):
        SchedulePlural.delete_all_from_db()
        return '', 204
