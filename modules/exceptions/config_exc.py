class ConfigBaseException(BaseException):
    message: str

    def __init__(self) -> None:
        super().__init__(self.message)


class ConfigFieldIsRequired(ConfigBaseException):
    def __init__(self, config_field: str) -> None:
        self.message = f"config field '{config_field}' is requiered, specify in .env"
        super().__init__()
