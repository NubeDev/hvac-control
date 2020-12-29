from src import db
from src.scheduler.scheduler_registry import SchedulerRegistry


class ScheduleModel(db.Model):
    """
    Table used to store Schedules in the database.
    """
    __tablename__ = "schedule"
    uuid = db.Column(db.String(80), primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(120), nullable=False)
    enable = db.Column(db.Boolean, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return "SensorModel({})".format(self.uuid)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def filter_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid)

    @classmethod
    def find_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def delete_all_from_db(cls):
        cls.query.delete()
        db.session.commit()
        SchedulerRegistry.get_instance().remove_all_schedules()

    def save_to_db(self):
        # self.sensor_store = SensorStoreModel.create_new_sensor_store_model(self.uuid)
        db.session.add(self)
        db.session.commit()
        # SchedulerRegistry.get_instance().add_schedule(self.schedule_id, self.uuid, self.name)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        SchedulerRegistry.get_instance().remove_schedule(self.schedule_id)




