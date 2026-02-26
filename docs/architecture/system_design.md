# OpenSight Pro - System Architecture

## Overview

OpenSight Pro is a modular sales intelligence platform built with a clean, scalable architecture.

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│                   (Streamlit Dashboard)                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Application Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Analytics   │  │  Reporting   │  │  Insights    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Data Layer                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │     ETL      │  │   Models     │  │  Services    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Storage Layer                             │
│              (SQLite / PostgreSQL)                          │
└─────────────────────────────────────────────────────────────┘
```

## Components

### 1. Frontend Layer

**Technology**: Streamlit

**Responsibilities**:
- User interface
- Data visualization
- File upload handling
- Filter management
- Data export

**Location**: `src/frontend/app.py`

### 2. Application Layer

#### Analytics Module
- KPI computation
- Trend analysis
- Channel attribution
- Funnel analysis

#### Reporting Module
- PDF generation
- Executive summaries
- Insight formatting
- Export functionality

#### Insights Module
- Pattern detection
- Anomaly identification
- Recommendations
- Trend analysis

**Location**: `src/backend/`

### 3. Data Layer

#### ETL (Extract, Transform, Load)
- Data ingestion from CSV/Excel
- Data cleaning and validation
- Deduplication
- Currency normalization

#### Models
- Data schemas
- Database models
- Relationships

#### Services
- Business logic
- KPI calculations
- Data aggregations

**Location**: `src/backend/etl/`, `src/backend/models/`, `src/backend/services/`

### 4. Storage Layer

**Default**: SQLite (development)
**Production**: PostgreSQL recommended

**Tables**:
- `raw_sales` - Raw sales data
- `processed_sales` - Cleaned sales data
- `kpis` - Computed KPIs
- `insights` - Generated insights

## Data Flow

### 1. Data Ingestion

```
User Upload
    ↓
File Validation
    ↓
CSV/Excel Parser
    ↓
Raw Data Storage
```

### 2. Data Processing

```
Raw Data
    ↓
Cleaning (remove nulls, duplicates)
    ↓
Validation (schema checks)
    ↓
Transformation (normalize, aggregate)
    ↓
Processed Data Storage
```

### 3. Analytics

```
Processed Data
    ↓
KPI Computation
    ↓
Trend Analysis
    ↓
Channel Attribution
    ↓
Insights Generation
```

### 4. Visualization

```
Analytics Results
    ↓
Formatting
    ↓
Visualization (Plotly)
    ↓
Dashboard Display
```

## Key Features

### Real-Time Analytics

- Instant KPI computation
- Live data updates
- Interactive filters

### Scalability

- Modular design
- Horizontal scaling ready
- Database agnostic

### Reliability

- Error handling
- Data validation
- Backup support

### Performance

- Caching mechanisms
- Optimized queries
- Lazy loading

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit 1.0+ |
| Visualization | Plotly, Matplotlib |
| Data Processing | Pandas, NumPy |
| Backend | Python 3.8+ |
| Database | SQLite / PostgreSQL |
| Containerization | Docker |
| Testing | Pytest |

## Design Patterns

### 1. Separation of Concerns

- Frontend handles UI
- Backend handles logic
- Data layer handles storage

### 2. Caching

```python
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')
```

### 3. Dependency Injection

Services receive dependencies through constructors

### 4. Factory Pattern

Data models created through factory methods

## Security Architecture

### Data Security

- Input validation
- SQL injection prevention
- XSS protection

### Application Security

- Error handling
- Secure defaults
- Logging and monitoring

### Infrastructure Security

- HTTPS in production
- Environment variables for secrets
- Regular updates

## Scalability Strategy

### Vertical Scaling

- Increase server resources
- Optimize code
- Cache aggressively

### Horizontal Scaling

- Multiple instances
- Load balancer
- Shared database
- Message queue (optional)

## Deployment Architecture

### Development

```
Local Machine
    ↓
Streamlit Dev Server
    ↓
SQLite Database
```

### Production

```
Cloud Provider
    ↓
Docker Container
    ↓
Reverse Proxy (Nginx)
    ↓
PostgreSQL Database
```

## API Design (Optional Backend)

### Endpoints

```
GET  /api/kpis/summary      - Get KPI summary
GET  /api/kpis/daily        - Get daily metrics
GET  /api/insights          - Get insights
POST /api/ingest/upload     - Upload data
POST /api/report/generate   - Generate report
```

## Error Handling

### User Errors

- Validation errors
- File format errors
- Missing data

### System Errors

- Database connection failures
- File I/O errors
- Processing errors

### Recovery

- Graceful degradation
- Error logging
- User notifications

## Monitoring & Logging

### Metrics

- Response time
- Error rate
- Data processing time
- User sessions

### Logs

- Application logs
- Error logs
- Access logs
- Audit logs

## Future Enhancements

### Phase 2

- Real-time data streaming
- Advanced ML models
- Multi-user support
- Custom dashboards

### Phase 3

- Mobile app
- API marketplace
- White-label option
- Enterprise features

---

For implementation details, see specific module documentation in `docs/`.
