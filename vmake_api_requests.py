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


        def create_task(self, image_url):
            """
            Создание задачи на обработку изображения.
            :param image_url: URL изображения для обработки.
            :return: ID задачи или None, если произошла ошибка.
            """
            data = {"image": image_url}
            headers = {"X-Api-Key": self.vmake_api_key}

            response = requests.post(self.base_url, json=data, headers=headers)
            if response.status_code != 200:
                print("Ошибка при создании задачи:", response.text)
                return None

            response_data = response.json()
            print("Ответ от сервера (создание задачи):", response_data)

            task_id = response_data.get("data", {}).get("taskId")
            if not task_id:
                print("Ошибка: не удалось получить ID задачи.")
                return None

            return task_id


        def check_task(self, task_id):
            """
            Проверка состояния задачи.
            :param task_id: ID задачи для проверки.
            :return: Ссылка на результат или None, если произошла ошибка.
            """
            url = f"{self.base_url}/{task_id}"
            headers = {"X-Api-Key": self.vmake_api_key}

            while True:
                response = requests.get(url, headers=headers)
                if response.status_code != 200:
                    print("Ошибка при проверке задачи:", response.text)
                    return None

                response_data = response.json()
                task_status = response_data.get("data", {}).get("status", "unknown")
                print(f"Статус задачи: {task_status}")

                if task_status == "success":
                    print("Задача успешно завершена!")
                    download_url = response_data["data"].get("downloadUrl")
                    if not download_url:
                        print("Ошибка: ссылка на результат отсутствует.")
                        return None
                    return download_url

                if task_status == "error":
                    print("Ошибка при обработке задачи:", response_data["data"].get("message", "Неизвестная ошибка"))
                    return None

                time.sleep(self.check_interval)