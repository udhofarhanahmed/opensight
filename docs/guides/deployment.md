# Deployment Guide

Deploy OpenSight Pro to production using various platforms.

## Local Development

```bash
streamlit run src/frontend/app.py
```

## Docker Deployment

### Build and Run

```bash
# Build image
docker build -f config/Dockerfile -t opensight-pro .

# Run container
docker run -p 8501:8501 opensight-pro
```

### Docker Compose

```bash
docker-compose -f config/docker-compose.yml up
```

## Streamlit Cloud (Recommended for Quick Start)

### Steps

1. Push code to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub repository
5. Select `src/frontend/app.py` as the main file
6. Deploy!

### Environment Variables

Set in Streamlit Cloud settings:

```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
```

## Heroku Deployment

### Prerequisites

- Heroku CLI installed
- Heroku account

### Steps

```bash
# Login to Heroku
heroku login

# Create app
heroku create opensight-pro

# Add Procfile
echo "web: streamlit run src/frontend/app.py --server.port=$PORT" > Procfile

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

## AWS Deployment

### Option 1: ECS (Elastic Container Service)

1. Build Docker image
2. Push to ECR (Elastic Container Registry)
3. Create ECS task definition
4. Deploy to ECS cluster

### Option 2: EC2

1. Launch EC2 instance
2. SSH into instance
3. Clone repository
4. Install dependencies
5. Run Streamlit

```bash
# On EC2 instance
git clone https://github.com/udhofarhanahmed/opensight.git
cd opensight
pip install -r requirements.txt
streamlit run src/frontend/app.py --server.port 80
```

## DigitalOcean App Platform

### Steps

1. Connect GitHub repository
2. Select `src/frontend/app.py` as entry point
3. Set environment variables
4. Deploy

## Environment Variables

Common environment variables for production:

```bash
# Streamlit
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ENABLEXSRFPROTECTION=false

# Application
ENVIRONMENT=production
DEBUG=false
```

## Security Considerations

### HTTPS

- Use reverse proxy (Nginx) for HTTPS
- Enable SSL certificates (Let's Encrypt)

### Authentication

- Add authentication layer (optional)
- Use environment variables for secrets

### Data

- Encrypt sensitive data
- Use secure connections
- Regular backups

## Performance Optimization

### Caching

```python
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')
```

### Lazy Loading

Load data only when needed

### Database

Use PostgreSQL for production instead of SQLite

## Monitoring

### Logs

Monitor application logs for errors

### Metrics

Track:
- Response time
- Error rate
- User sessions
- Data processing time

## Scaling

### Horizontal Scaling

- Deploy multiple instances
- Use load balancer
- Share database

### Vertical Scaling

- Increase server resources
- Optimize code
- Cache aggressively

## Backup & Recovery

### Backup Strategy

- Daily database backups
- Version control for code
- Document configurations

### Recovery

- Test recovery procedures
- Maintain backup archives
- Document recovery steps

## Cost Optimization

| Platform | Cost | Best For |
|----------|------|----------|
| Streamlit Cloud | Free | Development, demos |
| Heroku | $7-50/month | Small apps |
| AWS | Pay-as-you-go | Enterprise |
| DigitalOcean | $5-40/month | Small-medium apps |

## Troubleshooting

### App won't start

- Check logs
- Verify dependencies
- Test locally first

### Slow performance

- Enable caching
- Optimize queries
- Use CDN for assets

### Memory issues

- Reduce data size
- Implement pagination
- Use streaming

---

For more help, see [Getting Started](getting_started.md) or open an [issue](https://github.com/udhofarhanahmed/opensight/issues).
