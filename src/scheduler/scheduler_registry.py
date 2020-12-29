class SchedulerRegistry:
    __instance = None

    def __init__(self):
        if SchedulerRegistry.__instance:
            raise Exception("SchedulerRegistry class is a singleton class!")
        else:
            self.__schedules = {}
            SchedulerRegistry.__instance = self

    @staticmethod
    def get_instance():
        if SchedulerRegistry.__instance is None:
            SchedulerRegistry()
        return SchedulerRegistry.__instance

    def get_schedules(self):
        return self.__schedules

    def get_schedule(self, schedule) -> tuple:
        if self.__schedules[schedule]:
            return self.__schedules[schedule]
        return None, None

    def add_schedule(self, schedule, uuid, name):
        self.__schedules[schedule] = uuid, name

    def remove_schedule(self, schedule):
        self.__schedules.pop(schedule, None)

    def remove_all_schedules(self):
        self.__schedules = {}
