from fastapi import APIRouter, Depends
from app.dependencies import get_current_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def admin_dashboard(admin = Depends(get_current_admin)):
    return {"message": "Welcome Admin!"}