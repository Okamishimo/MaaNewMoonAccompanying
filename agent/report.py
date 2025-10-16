import requests


def punch_in():
    try:
        response = requests.post(
            "http://ts.codax.site/repo",
            json={"from": "mnma", "version": "v2.3.8"},
            headers={"Content-Type": "application/json"},
            timeout=3,
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return e
