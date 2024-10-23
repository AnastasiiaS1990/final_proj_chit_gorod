import requests


class AuthApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = "https://web-gate.chitai-gorod.ru/api/v1/"
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjgxMjE0MDEsImlhdCI6MTcyOTYyMTM0NSwiZXhwIjoxNzI5NjI0OTQ1LCJ0eXBlIjoyMH0.0EP8iidzthtNSozF3gVZVjogD_3n7d6QJ2ZNvmUxJm4"

    # def get_all_boards_by_org_id(self, org_id: str) -> dict:
    #     path = ("{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards".
    #             format(trello=self.base_url, id=org_id))
    #     cookie = {"token": self.token}
    #     resp = requests.get(path, cookies=cookie)
    #     return resp.json()