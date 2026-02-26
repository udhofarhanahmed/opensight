# Getting Started with OpenSight Pro

Welcome to OpenSight Pro! This guide will help you set up and start using the platform in minutes.

## Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- 500 MB disk space
- Basic familiarity with command line

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/udhofarhanahmed/opensight.git
cd opensight
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run src/frontend/app.py
```

The application will open automatically at `http://localhost:8501`

## First Steps

### 1. Load Sample Data

Click the **📊 Load Sample** button in the sidebar to populate the dashboard with demo data.

### 2. Explore the Dashboard

- **Dashboard Tab**: View KPIs and revenue trends
- **Analytics Tab**: Analyze data by product, channel, and status
- **Insights Tab**: Get key insights from your data
- **Data Tab**: Preview and export your data

### 3. Upload Your Own Data

To use your own data:

1. Prepare a CSV or Excel file with columns: `date`, `amount`
2. Optional columns: `channel`, `product`, `status`, `customer_id`
3. Click **📤 Upload Data** in the sidebar
4. Select your file
5. The data will be loaded and visualized

### 4. Use Filters

Once data is loaded, use the sidebar filters to:

- Filter by date range
- Select specific channels
- Filter by product
- Filter by order status

## File Format

### Required Columns

- **date** - Order date (YYYY-MM-DD format)
- **amount** - Order amount (numeric)

### Optional Columns

- **channel** - Marketing channel (e.g., Instagram, Facebook, Website)
- **product** - Product name
- **status** - Order status (e.g., Completed, Pending, Cancelled)
- **customer_id** - Customer identifier
- **order_id** - Order identifier

### Example CSV

```csv
date,amount,channel,product,status,customer_id
2026-02-01,150.00,Instagram,Product A,Completed,CUST001
2026-02-01,200.00,Website,Product B,Completed,CUST002
2026-02-02,75.50,Facebook,Product A,Pending,CUST003
```

## Features Overview

### Dashboard

- Real-time KPI tracking (Revenue, Orders, AOV, Conversion Rate)
- Daily revenue trends
- Channel performance analysis
- Interactive visualizations

### Analytics

- Revenue by product
- Order status distribution
- Channel performance comparison
- Custom data filtering

### Insights

- Data summary statistics
- Performance metrics
- Key trends and patterns

### Data Export

- Download as CSV
- Download as Excel
- Data preview

## Troubleshooting

### Application won't start

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Run again
streamlit run src/frontend/app.py
```

### Port already in use

```bash
# Run on different port
streamlit run src/frontend/app.py --server.port 8502
```

### File upload fails

- Ensure file is CSV or Excel format
- Check that required columns (`date`, `amount`) exist
- Verify data format is correct

## Next Steps

- Read the [User Guide](user_guide.md) for advanced features
- Check [Deployment Guide](deployment.md) for production setup
- Review [Architecture](../architecture/system_design.md) for technical details

## Getting Help

- **Issues**: Report bugs on [GitHub Issues](https://github.com/udhofarhanahmed/opensight/issues)
- **Discussions**: Ask questions on [GitHub Discussions](https://github.com/udhofarhanahmed/opensight/discussions)
- **Documentation**: See [docs/](../) directory

---

**Happy analyzing! 📊**
