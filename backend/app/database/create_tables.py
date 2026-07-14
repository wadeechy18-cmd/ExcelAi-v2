from app.database.base import Base
from app.database.session import engine

# Import all models here
from app.models.user import User  # noqa: F401


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")