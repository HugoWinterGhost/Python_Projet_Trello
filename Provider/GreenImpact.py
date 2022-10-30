import sys

from dotenv import dotenv_values
from requests import post, delete, patch, get
import urllib3

from .Discord import Discord


class GreenImpact:
    def __init__(self) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.host = dotenv_values(".env")["HOST"]
        self.login = {
            "email": dotenv_values(".env")["EMAIL"],
            "password": dotenv_values(".env")["PASSWORD"]
        }
        self.headers = {
            "Authorization": f"Bearer {self.__connection()}"
        }

    def __connection(self) -> None:
        res = post(
            f"{self.host}authentication_token",
            json=self.login,
            verify=False
        )
        if res.status_code == 200:
            return res.json()["token"]
        Discord().post_error("__connection", res.json())
        print(res.json())
        sys.exit()

    def get_all(self, entity: str, filter: dict = None) -> (dict, list):
        res = get(
            f"{self.host}{entity}",
            params=filter,
            headers=self.headers,
            verify=False
        )
        if res.status_code == 200:
            return res.json()["hydra:member"]
        Discord().post_error(f"get_all({entity})", res.json()["description"])
        print(res.json())

    def delete(self, entity: str, entity_id: (int, str)) -> dict:
        res = delete(
            f"{self.host}{entity}/{entity_id}",
            headers=self.headers,
            verify=False
        )
        if res.status_code == 204:
            return {}
        Discord().post_error(f"delete({entity}, {entity_id})", res.json()["description"])
        print(res.json())

    def update(self, entity: str, entity_id: (int, str), data: dict) -> dict:
        """
        Update Entity

        Args:
            entity:
            entity_id:
            data:

        Returns:
            dict
        """
        headers = self.headers.copy()
        headers["Content-Type"] = "application/merge-patch+json"
        res = patch(
            f"{self.host}{entity}/{entity_id}",
            headers=headers,
            json=data,
            verify=False
        )

        if res.status_code == 200:
            return res.json()
        Discord().post_error(f"update({entity}, {entity_id}, {data})", res.json()["description"])
        print(res.json())
