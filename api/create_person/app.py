from spin_sdk.http import IncomingHandler, Request, Response
from spin_sdk.postgres import open
from spin_sdk.variables import get
import json

class IncomingHandler(IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        if request.method == "POST" \
           and request.headers["content-type"] == "application/json" \
           and request.body is not None:
            print(request.body)
            person = json.loads(request.body)
            print(person)
            with open(f"user={get("postgres_user")} password={get("postgres_password")} dbname={get("postgres_db")} host={get("postgres_host")}") as db:
                query = f"INSERT INTO person (last_name, phone_number) VALUES ('{person.get('last_name')}', '{person.get('phone_number')}');"
                print(query)
                db.execute(query, [])
        return Response(
            200,
            {"content-type": "text/plain"},
            bytes("Person successfully created", "utf-8")
        )
