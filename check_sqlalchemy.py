import sqlalchemy
print("sqlalchemy file:", getattr(sqlalchemy, "__file__", "<none>"))
print("sqlalchemy version:", getattr(sqlalchemy, "__version__", "<none>"))
try:
    from sqlalchemy.orm import properties
    print("imported properties OK")
except Exception as e:
    print("import error:", type(e).__name__, e)