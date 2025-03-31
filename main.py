from fastapi import FastAPI, HTTPException, Query
from datetime import datetime, timezone
from db import get_db_connection

app = FastAPI()

@app.get("/validate")
def validate_license(email: str = Query(...), machine_id: str = Query(...)):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT machine_key, subscription_expiry, is_active 
                FROM users 
                WHERE LOWER(email) = LOWER(%s)
                """, (email,))

    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="License not found")

    machine_key_db, expiry_date, is_active = row

    # BLOCK if machine ID mismatches
    if machine_key_db and machine_key_db != machine_id:
        raise HTTPException(status_code=403, detail="License already used on another machine")

    # Save machine ID if first time
    if not machine_key_db:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    UPDATE users 
                    SET machine_key = %s 
                    WHERE LOWER(email) = LOWER(%s)
                    """, (machine_id, email))
        conn.commit()
        cur.close()
        conn.close()

    # Check expiry
    if expiry_date and datetime.now(timezone.utc).date() > expiry_date:
        raise HTTPException(status_code=403, detail="License expired")

    # Check active status
    if not is_active:
        raise HTTPException(status_code=403, detail="License inactive")

    return { "status": "valid" }
