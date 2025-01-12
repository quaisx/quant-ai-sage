**WORK IN PROGRESS**
*NOTE:* this is an actively developed project that is not yet functional by any means.

![Quant AI Sage](img/quant-ai-sage.jpeg)
# Quant-AI-Sage

Quant-AI-Sage is a modular, Python-based stock trading platform designed for predictive trading powered by technical analysis and advanced machine learning. The system is built with flexibility and accuracy as its core goals, allowing users to perform in-depth technical analysis, leverage large language models (LLMs) for stock trend prediction, and automate trading decisions through integrated broker APIs.

---

## **Key Features**
- **Real-Time Data Ingestion**: Fetch and preprocess real-time stock market data from multiple sources.
- **Historical Data Management**: Store and manage historical stock data in a relational database (SQLite initially, PostgreSQL for scalability).
- **Technical Analysis**: Calculate technical indicators (e.g., RSI, moving averages) for feature generation.
- **AI-Powered Predictions**: Use LLMs to analyze patterns and predict stock price movements.
- **Automated Trading**: Place buy/sell orders based on predictions, integrated with risk management controls.
- **Highly Modular Architecture**: Each module is independent, making the system easy to extend or customize.

---

## **System Architecture**

Quant-AI-Sage is divided into six main functional layers:

1. **Data Ingestion Layer**:
   - Fetches real-time trading data via REST APIs.
   - Preprocesses data for analysis and storage.

2. **Data Storage Layer**:
   - Stores historical stock data in a relational database.
   - Provides APIs for reading and writing data.

3. **Technical Analysis Module**:
   - Performs technical analysis to generate indicators.
   - Features a scheduler for periodic analysis.

4. **Prediction Engine**:
   - Uses LLMs for stock trend prediction.
   - Prepares features and post-processes predictions for downstream usage.

5. **Trading Module**:
   - Places trades using broker APIs based on AI predictions.
   - Implements risk management to ensure safe trading.

6. **Message Bus (Optional)**:
   - Provides a pub/sub mechanism to decouple modules and support scalability.
   - Enables asynchronous communication between components.

---

## **Technologies Used**

### **Programming Language**
- Python: Chosen for its rich ecosystem of libraries, ease of use, and community support.

### **Core Libraries and Frameworks**
- **Data Handling**: `pandas`, `numpy`
- **Database**: `sqlite3` (initial), `psycopg2` (PostgreSQL for production)
- **Technical Analysis**: `TA-Lib`, `pyti`
- **Machine Learning**: `transformers`, `scikit-learn`
- **API Integration**: `requests`
- **Asynchronous Communication**: `kombu`, `pika` (RabbitMQ)

### **DevOps and Testing**
- **Testing**: `pytest`
- **Code Quality**: `black`, `flake8`, `mypy`
- **Containerization**: Docker (optional, for deployment)

---

## **Getting Started**

### **Prerequisites**
- Python 3.12 or higher
- Virtual environment tools (e.g., `venv`, `conda`)
- SQLite (pre-installed with Python)
- (Optional) PostgreSQL for scalable storage

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/quaisx/quant-ai-sage.git
   cd quant-ai-sage
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the configuration file:
   - Copy `config/settings.example.yaml` to `config/settings.yaml`.
   - Update API keys, database settings, and other parameters as needed.

4. Run the application:
   ```bash
   python -m quant_ai_sage.app
   ```

---

## **Project Structure**
```
quant_ai_sage/
├── quant_ai_sage/                # Main application package
│   ├── ingestion/                # Data ingestion components
│   ├── storage/                  # Database-related modules
│   ├── analysis/                 # Technical analysis modules
│   ├── prediction/               # Prediction engine and LLM integration
│   ├── trading/                  # Trading logic and broker APIs
│   └── messaging/                # Optional pub/sub communication
├── docs/                         # Documentation files
├── config/                       # Configuration files
├── data/                         # Example or mock data
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview
```

---

## **Future Enhancements**
- Support for multiple LLM backends and custom fine-tuning.
- Enhanced risk management and portfolio optimization.
- Real-time dashboards for visualizing predictions and trades.
- Scalability improvements with container orchestration (e.g., Kubernetes).

---

## **Contributing**
Contributions are welcome! Please submit a pull request or create an issue for any bugs or feature requests.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

