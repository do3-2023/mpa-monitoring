from spin_sdk.http import IncomingHandler, Request, Response
from spin_sdk.postgres import open
from spin_sdk.variables import get

class IncomingHandler(IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        persons = []
        try:
            # Establishing the database connection
            with open(f"user={get("postgres_user")} password={get("postgres_password")} dbname={get("postgres_db")} host={get("postgres_host")}") as db:
                result = db.query("select * from person", [])
                rows = result.rows
                for row in rows:
                    persons.append([row[0].value, row[1].value, row[2].value])
                print(persons)
        except Exception as err1:
            raise RuntimeError("Error retrieving records from the database") from err1

        return Response(
            200,
            {"content-type": "application/json"},
            bytes(str(persons), "utf-8")
        )
