from fastapi import FastAPI, HTTPException
import sqlite3
from model import text_to_sql

app = FastAPI()


from pydantic import BaseModel

class QueryRequest(BaseModel):
    x: str


@app.post("/query")
async def query_database(query: QueryRequest):
    try:
        sql_query = text_to_sql(query.x)
        print(sql_query)

        conn = sqlite3.connect("mock_database.db")
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()

        return {"query": sql_query, "result": result}
    except Exception as e:
        print(f"Error: {str(e)}")  # Add this line to debug
        raise HTTPException(status_code=400, detail=str(e))


