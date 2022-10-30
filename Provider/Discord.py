from requests import post
from dotenv import dotenv_values


class Discord:

    def post_error(self, function: str, error: (list, dict, str)) -> None:
        """
        Post an message on discord

        Args:
            function:
            error:

        Returns:
            None
        """
        post(
            dotenv_values(".env")["BOT_URL"],
            headers={
                "Content-Type": "application/json"
            },
            json={
                "embeds": [{
                    "title": f":warning: Error with {function}",
                    "description": error,
                    "color": "14423100"
                }]
            }
        )