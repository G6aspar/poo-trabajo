class ConfigSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            cls._instance.config_value = "Default Config"
        return cls._instance

    def get_config_value(self):
        return self.config_value

    def set_config_value(self, value):
        self.config_value = value
