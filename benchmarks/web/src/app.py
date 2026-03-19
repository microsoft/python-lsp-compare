from flask import Flask, request
import requests


app = Flask(__name__)
client = requests.Session()


@app.get("/users")
def users() -> dict[str, object]:
    response = client.get("https://example.invalid/users", params=request.args)
    return {"status": response.status_code}
