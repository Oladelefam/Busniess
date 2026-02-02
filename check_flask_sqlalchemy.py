import flask, sqlalchemy
print("Flask", getattr(flask, "__version__", "<none>"))
print("SQLAlchemy", getattr(sqlalchemy, "__version__", "<none>"))
try:
    import flask_sqlalchemy
    print("flask_sqlalchemy", getattr(flask_sqlalchemy, "__version__", "<none>"))
    from flask_sqlalchemy import SQLAlchemy
    print("Imported SQLAlchemy from flask_sqlalchemy OK")
except Exception as e:
    print("import error:", type(e).__name__, e)