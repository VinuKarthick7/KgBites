# Docker Setup Instructions

This Docker Compose configuration sets up a complete development environment with:
- PostgreSQL database
- Django backend API
- React frontend application

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. **Clone the repository and navigate to the project directory:**
   ```bash
   cd KgBites
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your preferred values.

3. **Build and start all services:**
   ```bash
   docker-compose up --build
   ```

4. **Access the applications:**
   - Frontend (React): http://localhost:3000
   - Backend (Django): http://localhost:8000
   - PostgreSQL: localhost:5432

## Services

### PostgreSQL Database
- **Container**: `kgbites_postgres`
- **Port**: 5432
- **Database**: `kgbites_db`
- **User**: `kgbites_user`
- **Password**: Set via `DB_PASSWORD` in `.env`

### Django Backend
- **Container**: `kgbites_backend`
- **Port**: 8000
- **API**: http://localhost:8000

### React Frontend
- **Container**: `kgbites_frontend`
- **Port**: 3000
- **URL**: http://localhost:3000

## Development Commands

### Start services in background:
```bash
docker-compose up -d
```

### Stop all services:
```bash
docker-compose down
```

### View logs:
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs backend
docker-compose logs frontend
docker-compose logs postgres
```

### Run Django management commands:
```bash
# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Run migrations
docker-compose exec backend python manage.py migrate

# Collect static files
docker-compose exec backend python manage.py collectstatic
```

### Access database:
```bash
docker-compose exec postgres psql -U kgbites_user -d kgbites_db
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DB_PASSWORD=your_secure_password

# Django Configuration
DEBUG=1

# Frontend Configuration
REACT_APP_API_URL=http://localhost:8000
```

## Data Persistence

PostgreSQL data is persisted in a Docker volume named `postgres_data`. This means your database will survive container restarts.

To completely reset the database:
```bash
docker-compose down -v
docker-compose up --build
```

## Troubleshooting

1. **Port conflicts**: If ports 3000, 8000, or 5432 are already in use, modify the port mappings in `docker-compose.yml`

2. **Permission issues**: If you encounter permission issues, ensure your user has access to Docker

3. **Database connection issues**: Make sure the PostgreSQL service is fully started before Django tries to connect. The compose file includes health checks to handle this.

4. **Frontend not connecting to backend**: Check that the `REACT_APP_API_URL` environment variable is correctly set in your `.env` file