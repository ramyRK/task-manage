class AppConfigSingleton:
    _instance=None

    @staticmethod
    def get_instance():
        if AppConfigSingleton._instance is None:
            AppConfigSingleton()
        return AppConfigSingleton._instance

    def __init__(self):
        if AppConfigSingleton._instance is not None:
            raise Exception("this class is a singleton!")
        else:
            self.config_data = "Some configuration data"
            AppConfigSingleton._instance=self      