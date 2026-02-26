# OpenSight Pro

**Professional Sales Intelligence Platform | Free • Open Source • Enterprise-Grade**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)](https://streamlit.io)

```
 ██████╗ ██████╗ ███████╗███╗   ██╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║
██║   ██║██████╔╝█████╗  ██╔██╗ ██║
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║
╚██████╔╝██║     ███████╗██║ ╚████║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝

 ██████╗ ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗
██████╔╝██████╔╝██║   ██║
██╔═══╝ ██╔══██╗██║   ██║
██║     ██║  ██║╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
```

---

## 🎯 Overview

**OpenSight Pro** is a production-ready sales intelligence platform that transforms raw sales data into actionable insights. Built entirely with free, open-source technologies, it provides real-time analytics, predictive modeling, and automated reporting for SMEs and enterprises.

### Key Capabilities

- **Real-Time Analytics** - 15+ KPIs computed instantly from your data
- **Predictive Intelligence** - ML-powered lead scoring and conversion forecasting
- **Automated Reporting** - PDF reports with insights and recommendations
- **Multi-Channel Attribution** - Understand performance across all marketing channels
- **Funnel Analysis** - Identify and fix sales bottlenecks
- **Zero Infrastructure Costs** - Runs locally or on any cloud provider

---

## ⚡ Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or conda
- 500 MB disk space

### Installation (5 minutes)

```bash
# Clone the repository
git clone https://github.com/udhofarhanahmed/opensight.git
cd opensight

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run src/frontend/app.py
```

The application will open at `http://localhost:8501`

---

## 🚀 Features

### 📊 Dashboard & Analytics

- **Real-time KPI Tracking** - Revenue, conversion rates, customer acquisition cost, lifetime value
- **Interactive Visualizations** - Charts, funnels, and trends powered by Plotly
- **Custom Filters** - Slice data by date, channel, product, and status
- **Data Export** - Download filtered data as CSV or Excel

### 🤖 Machine Learning

- **Lead Scoring** - Predict conversion probability for each lead
- **Churn Prediction** - Identify at-risk customers before they leave
- **Anomaly Detection** - Automatic alerts for unusual patterns
- **Feature Importance** - Understand what drives conversions

### 📑 Reporting

- **Automated PDF Reports** - Executive summaries with insights
- **Leakage Analysis** - Identify where leads are dropping off
- **Channel Performance** - ROI and efficiency metrics by channel
- **Recommendations** - Actionable next steps for optimization

### 🔄 Data Integration

- **CSV/Excel Upload** - Simple file-based data import
- **Data Validation** - Automatic schema and quality checks
- **Deduplication** - Remove duplicate records automatically
- **Currency Handling** - Support for multiple currencies

---

## 📁 Project Structure

```
opensight/
├── src/
│   ├── backend/              # Core analytics engine
│   │   ├── etl/             # Data pipelines
│   │   ├── models/          # Data models
│   │   ├── services/        # Business logic
│   │   ├── insights/        # Insight generation
│   │   └── api/             # API endpoints
│   ├── frontend/            # Streamlit application
│   └── shared/              # Shared utilities
├── tests/                   # Test suites
├── config/                  # Configuration files
├── docs/                    # Documentation
├── scripts/                 # Utility scripts
├── assets/                  # Logos and branding
└── sample_data/             # Example datasets
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit 1.0+ |
| **Backend** | Python 3.8+, FastAPI (optional) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib |
| **Machine Learning** | Scikit-learn, LightGBM |
| **Database** | SQLite (default), PostgreSQL (optional) |
| **Containerization** | Docker, Docker Compose |
| **Testing** | Pytest |

---

## 📖 Documentation

- **[Getting Started Guide](docs/guides/getting_started.md)** - Step-by-step setup instructions
- **[User Guide](docs/guides/user_guide.md)** - How to use the application
- **[Architecture](docs/architecture/system_design.md)** - System design and components
- **[API Documentation](docs/api/endpoints.md)** - REST API reference
- **[Deployment Guide](docs/guides/deployment.md)** - Production deployment options
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute

---

## 🚢 Deployment

### Local Development

```bash
streamlit run src/frontend/app.py
```

### Docker

```bash
docker-compose -f config/docker-compose.yml up
```

### Cloud Deployment

- **Streamlit Cloud** - Free hosting at https://streamlit.io/cloud
- **Heroku** - Deploy with `git push heroku main`
- **AWS** - ECS, Lambda, or EC2
- **DigitalOcean** - App Platform or Droplets

See [Deployment Guide](docs/guides/deployment.md) for detailed instructions.

---

## 📊 Sample Data

The repository includes sample sales data with:

- 1,000+ sales records
- 6 marketing channels (Instagram, WhatsApp, Website, Facebook, Google Ads, Referral)
- 90 days of historical data
- Realistic conversion patterns

Load sample data in the application sidebar: **📊 Sample Data** button.

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/unit/test_analytics.py -v
```

---

## 🔐 Security

- **No Sensitive Data** - Platform handles only business metrics
- **Data Privacy** - All data stays on your infrastructure
- **HTTPS Ready** - Secure connections in production
- **Input Validation** - All inputs validated and sanitized
- **GDPR Compliant** - Data deletion and export capabilities

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone and setup
git clone https://github.com/udhofarhanahmed/opensight.git
cd opensight
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

# Make changes and run tests
pytest tests/

# Submit pull request
```

---

## 💬 Support

- **Documentation** - See [docs/](docs/) directory
- **Issues** - Report bugs on [GitHub Issues](https://github.com/udhofarhanahmed/opensight/issues)
- **Discussions** - Ask questions on [GitHub Discussions](https://github.com/udhofarhanahmed/opensight/discussions)

---

## 🎯 Roadmap

### Version 1.1 (Q1 2026)
- [ ] Multi-user authentication
- [ ] Custom dashboards
- [ ] Advanced ML models
- [ ] API rate limiting

### Version 2.0 (Q2 2026)
- [ ] Real-time data streaming
- [ ] Mobile app
- [ ] Advanced forecasting
- [ ] Team collaboration

### Version 3.0 (Q3 2026)
- [ ] AI-powered insights
- [ ] Custom integrations
- [ ] Enterprise features
- [ ] White-label option

---

## 📈 Use Cases

**For SME Owners:**
- Real-time visibility into sales performance
- Data-driven decision making
- Automated insights and recommendations

**For Sales Teams:**
- Lead scoring and prioritization
- Funnel bottleneck identification
- Performance tracking by channel

**For Marketing Teams:**
- ROI tracking by channel
- Budget optimization recommendations
- Campaign performance analysis

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Guide](https://pandas.pydata.org/docs/)
- [Plotly Tutorial](https://plotly.com/python/)
- [Machine Learning with Scikit-learn](https://scikit-learn.org/stable/)

---

## 📊 Performance

- **Data Processing** - Handles 100K+ records in <5 seconds
- **Dashboard Load** - Initial load in <2 seconds
- **Report Generation** - PDF generation in <10 seconds
- **Memory Usage** - <500 MB for typical datasets

---

## 🌟 Features Comparison

| Feature | OpenSight Pro | Tableau | Looker |
|---------|---|---|---|
| **Cost** | Free | $70+/user/month | $2,000+/month |
| **Setup Time** | 5 minutes | 1-2 weeks | 2-4 weeks |
| **Open Source** | ✅ | ❌ | ❌ |
| **Customizable** | ✅ | ⚠️ | ⚠️ |
| **Self-Hosted** | ✅ | ❌ | ⚠️ |
| **ML Integration** | ✅ | ⚠️ | ⚠️ |

---

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) - App framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Plotly](https://plotly.com/) - Visualizations
- [Scikit-learn](https://scikit-learn.org/) - Machine learning

---

## 📞 Contact

- **GitHub** - [@udhofarhanahmed](https://github.com/udhofarhanahmed)
- **Issues** - [GitHub Issues](https://github.com/udhofarhanahmed/opensight/issues)
- **Discussions** - [GitHub Discussions](https://github.com/udhofarhanahmed/opensight/discussions)

---

**Built with ❤️ using free, open-source tools.**

**Zero cost. Maximum impact. Enterprise-grade.**

⭐ If you find this project helpful, please star it on GitHub!
