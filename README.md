# docker-terraform
Virtual Environments and Data Pipelines


# Docker & Terraform Repository

A comprehensive project repository exploring virtual environments, containerization with Docker, data pipelines, and Infrastructure as Code using Terraform.

## 📁 Repository Structure

### 1. **docker-sql/** - Docker and SQL Data Pipelines
Contains multiple projects for containerizing data ingestion pipelines and working with PostgreSQL databases.

#### **data-ingestion/**
- Python-based data ingestion application
- Technologies: Pandas, SQLAlchemy, psycopg2
- Features: Database operations, data transformation
- Requirements: Python ≥3.13

#### **docker-compose/**
- Docker Compose setup for multi-container applications
- Includes PostgreSQL database container configuration
- Data ingestion scripts with Docker orchestration
- Technologies: Click, Pandas, SQLAlchemy, psycopg2

#### **dockerizing-ingestion/**
- Pipeline project with Dockerfile
- Containerized data ingestion workflow
- Complete pipeline setup for production environments

#### **postgres-docker/**
- PostgreSQL database setup using Docker
- NYC taxi data ingestion
- Database initialization and configuration

#### **pgadmin/**
- PgAdmin container for PostgreSQL management
- Web-based database administration interface
- Configuration and setup scripts

#### **virtual-environment/**
- Dockerfile-based virtual environment setup
- Includes pipeline scripts
- Development environment configuration

#### **docker/test/**
- Testing utilities and test files
- File listing and Docker testing scripts

### 2. **homework/** - Course Assignments & Projects
Data engineering homework assignments using Docker and Terraform.

**Project Details:**
- NYC Taxi Data Processing
- Docker-based data pipeline
- Terraform Infrastructure as Code configuration
- SQL queries for data analysis
- Technologies: Click, Pandas, SQLAlchemy, psycopg2, PyArrow

**Key Features:**
- Data loading and transformation
- Docker containerization
- GCP infrastructure setup via Terraform
- Taxi zone lookup data

### 3. **terraform/** - Infrastructure as Code
Terraform configurations for cloud infrastructure management.

#### **learn-terraform-gcp/**
- Educational Terraform examples
- GCP-specific configurations

#### **terraform-gcp/**
- Production Terraform configurations for Google Cloud Platform
- Main infrastructure setup
- Variables and outputs configuration
- State files for environment tracking

#### **terraform_basic/**
- Basic Terraform configurations
- Foundation templates for IaC

#### **dev/**
- Development environment credentials (key files)
- GCP service account keys

## 🛠️ Technologies & Dependencies

### Core Technologies
- **Python** (3.12+)
- **Docker** - Container management
- **Docker Compose** - Multi-container orchestration
- **PostgreSQL** - Relational database
- **Terraform** - Infrastructure as Code
- **Google Cloud Platform (GCP)** - Cloud infrastructure

### Python Dependencies
- **pandas** - Data manipulation and analysis
- **SQLAlchemy** - SQL toolkit and ORM
- **psycopg2** - PostgreSQL adapter for Python
- **click** - Command-line interface creation
- **jupyter** - Interactive notebooks
- **pgcli** - PostgreSQL command-line client
- **PyArrow** - Apache Arrow Python bindings

## 🚀 Getting Started

### Prerequisites
- Python 3.12+ (3.13+ recommended)
- Docker & Docker Compose
- Terraform
- GCP account (for cloud projects)

### Running a Project

1. **Navigate to project directory:**
   ```bash
   cd docker-sql/docker-compose/



Environment Setup
Each project can use either traditional virtual environments or Docker containers:

See virtual-environment/ for Dockerfile-based setup
Use Python venv for traditional virtual environments


### Data Ingestion Workflow
The repository demonstrates a complete ETL (Extract, Transform, Load) pipeline:

### Data extraction (taxi trip data)
Transformation using Pandas
Loading into PostgreSQL
Management via PgAdmin
Infrastructure provisioning with Terraform