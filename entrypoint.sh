#!/bin/sh
set -e

echo "⏳ Waiting for Postgres to be ready..."

until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
  sleep 1
done

echo "✅ Postgres is ready. Running DB migrations..."

# Import models so they are included in metadata
python -c "from database import Base, engine; import models; Base.metadata.create_all(bind=engine)"

echo "🚀 Starting FastAPI server..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
