# QuantFlow

A real-time market data and trading strategy platform that ingests live market data, computes technical indicators, stores time-series data, runs rule-based trading strategies, and provides a REST API with monitoring capabilities.

## Features

- **Real-time Data Ingestion**: Stream live market data from multiple sources
- **Technical Indicators**: Compute indicators in real-time for analysis
- **Time-Series Storage**: Efficiently store and query historical price data
- **Trading Strategies**: Implement and backtest rule-based trading strategies
- **REST API**: Access data and control strategies via HTTP endpoints
- **Monitoring Dashboard**: Visualize market data and strategy performance

## Project Structure

```
quantflow/
├── data_ingestion/    # Real-time market data streaming and ingestion
├── processing/        # Technical indicators and data transformation
├── storage/           # Time-series database operations
├── strategy/          # Trading strategies and backtesting engine
├── api/              # REST API and monitoring dashboard
tests/                # Test suite
```

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Note**: Some dependencies like `ta-lib` require additional system libraries. Install TA-Lib first:
- macOS: `brew install ta-lib`
- Ubuntu/Debian: `sudo apt-get install libta-lib-dev`
- See [TA-Lib installation guide](https://github.com/mrjbq7/ta-lib#installation) for other platforms

### 3. Verify installation

```bash
python -c "import quantflow; print(quantflow.__version__)"
```

## Development

### Run tests

```bash
pytest
```

### Code formatting and linting

```bash
ruff check .
ruff format .
```

## Getting Started

This is a starter template. Build your modules in the respective directories:
- Add data source connectors in `quantflow/data_ingestion/`
- Implement indicators in `quantflow/processing/`
- Set up your database in `quantflow/storage/`
- Create strategies in `quantflow/strategy/`
- Build API endpoints in `quantflow/api/`

## License

MIT
