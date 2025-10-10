import requests


def punch_in():
    try:
        response = requests.post(
            "http://ts.codax.site/repo?from=mnma",
            json={"from": "mnma", "version": "v2.3.5"},
            headers={"Content-Type": "application/json"},
            timeout=5,
        )
        response.raise_for_status()

        try:
            return response.json()
        except ValueError:
            return {"response_text": response.text}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
