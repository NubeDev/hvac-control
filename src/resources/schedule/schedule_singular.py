from flask_restful import abort, marshal_with, reqparse
from src.models.schedule.model_schedule import ScheduleModel
from src.resources.schedule.mod_fields import schedule_fields
from src.resources.schedule.schedule_base import ScheduleBase


class ScheduleSingular(ScheduleBase):
    parser_patch = reqparse.RequestParser()
    parser_patch.add_argument('name', type=str, required=False)
    parser_patch.add_argument('description', type=str, required=False)
    parser_patch.add_argument('enable', type=bool, required=False)
    parser_patch.add_argument('enable_rest', type=bool, required=False)
    parser_patch.add_argument('mqtt_topic', type=str, required=False)
    parser_patch.add_argument('schedule', type=str, required=False)

    @marshal_with(schedule_fields)
    def get(self, uuid):
        sch = ScheduleModel.find_by_uuid(uuid)
        if not sch:
            abort(404, message='Schedule is not found')
        return sch

    @marshal_with(schedule_fields)
    def patch(self, uuid):
        data = ScheduleSingular.parser_patch.parse_args()
        sch = ScheduleModel.find_by_uuid(uuid)
        if sch is None:
            abort(404, message="Does not exist {}".format(uuid))
        try:
            non_none_data = {}
            for key in data.keys():
                if data[key] is not None:
                    non_none_data[key] = data[key]
            return self.update_schedule(uuid, non_none_data)
        except Exception as e:
            abort(500, message=str(e))

    def delete(self, uuid):
        sch = ScheduleModel.find_by_uuid(uuid)
        if sch:
            sch.delete_from_db()
        return '', 204
