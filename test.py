import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from main import app, get_db
from database import Base
import models

# Shared in-memory DB across threads
DATABASE_URL = "sqlite:///file::memory:?cache=shared"

# Create engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



# Apply override
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={
    "email": "qwe@example.com",
    "full_name": "string",
    "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "qwe@example.com"
    assert "id" in data

def test_login_user():
    response = client.post("/login", json={
        "email": "qwe@example.com",
        "password": "password"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
