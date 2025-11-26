from fastapi import FastAPI, HTTPException
from app.routers import user_router
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)


def check_database_connection():
    db = SessionLocal()
    try:
        # Execute a simple query to check the connection
        db.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError as e:
        print(f"Database connection error: {e}")
        return False
    finally:
        db.close()

@app.get("/health")
async def health_check():
    if check_database_connection():
        return {"status": "OK", "message": "Database connection successful."}
    else:
        raise HTTPException(status_code=500, detail="Database connection failed.")
    
@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)
