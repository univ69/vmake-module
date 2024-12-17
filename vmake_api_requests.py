import requests
import time


class VmakeAPI:
    def __init__(self, vmake_api_key, base_url="https://open.vmake.ai/api/v1/image/quality-enhance", check_interval=5):
        """
        Инициализация класса.
        :param vmake_api_key: API-ключ для аутентификации.
        :param base_url: URL для API Vmake.
        :param check_interval: Интервал проверки статуса задачи в секундах.
        """
        self.vmake_api_key = vmake_api_key
        self.base_url = base_url
        self.check_interval = check_interval