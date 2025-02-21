
# Masumi Network Agent Template

A production-ready template for building and deploying AI agents on the Masumi Network using CrewAI, FastAPI, and PostgreSQL.

## 🌟 Features

- MIP-003 compliant API endpoints
- Async database operations with SQLAlchemy
- CrewAI integration for agent orchestration
- Docker containerization
- Database migrations with Alembic
- Comprehensive logging
- Health monitoring
- Payment integration ready

## 🚀 Quick Start

1. **Clone the repository**
git clone https://github.com/yourusername/masumi-agent-template
cd masumi-agent-template



2. **Set up environment variables**

cp .env.example .env
Edit .env with your credentials:
- OPENAI_API_KEY
- MASUMI_AGENT_ID
- MASUMI_API_KEY
- DATABASE_URL


3. **Run with Docker**
docker-compose up --build



4. **Run migrations**
alembic upgrade head


## 🏗️ Project Structure
├── src/                  # Source code
│   ├── api/              # API endpoints and models
│   ├── core/             # Core configuration
│   ├── crew/             # CrewAI agents and tasks
│   └── db/               # Database models and session
├── alembic/              # Database migrations
├── tests/                # Test suite
└── docker-compose.yml    # Docker configuration



## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `MASUMI_AGENT_ID`: Your Masumi Network agent ID
- `MASUMI_API_KEY`: Your Masumi Network API key
- `DATABASE_URL`: PostgreSQL connection string

### Database Migrations

Create a new migration:
alembic revision -m "description"

Apply migrations:
alembic upgrade head

Rollback migration:
alembic downgrade -1


## 📚 API Documentation

### Endpoints

- `POST /api/v1/start_job`
  - Start a new agent job
  - Returns job ID and payment information

- `GET /api/v1/status`
  - Check job status
  - Returns current status and results if complete

- `GET /api/v1/availability`
  - Check service availability

- `GET /api/v1/input_schema`
  - Get expected input format

### Example Usage
python
import requests
Start a job
response = requests.post(
"http://localhost:8000/api/v1/start_job",
json={"input_data": {"param": "value"}}
)
job_id = response.json()["job_id"]
Check status
status = requests.get(
f"http://localhost:8000/api/v1/status?job_id={job_id}"
)



## 🚢 Deployment

### Digital Ocean

1. Update `app.yaml` with your configuration
2. Deploy using Digital Ocean App Platform:
doctl apps create --spec app.yaml



### Manual Deployment

1. Build Docker image:
docker build -t masumi-agent 

2. Run container:
docker run 



## 🔍 Monitoring

- Health check endpoint: `/health`
- Logging: Check container logs or `logs/` directory
- Database monitoring: Use pgAdmin or similar tools

## 🛠️ Development

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker & Docker Compose

### Local Development

1. Create virtual environment:
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows


2. Install dependencies:
pip install -r requirements.txt

3. Run development server:
uvicorn src.service:app --reload


### Running Tests
pytest tests/


## 📝 License

MIT License - see LICENSE file

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📮 Support

- GitHub Issues
- Documentation: [docs/](./docs)
- Email: your.email@example.com