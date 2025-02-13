# Text-to-SQL Query Generator

A conversational AI system that converts natural language queries into SQL and executes them against a database, featuring a Streamlit frontend and FastAPI backend.

<img src="text-to-sql-generator.jpg" width=500, height=500, align='center'>

## 🌟 Features

- Natural language to SQL conversion
- Interactive web interface using Streamlit
- RESTful API backend with FastAPI
- SQLite database integration
- Dynamic data visualization
- Mock database with sample business data

## 🏗️ Architecture

The project consists of three main components:
1. **Frontend**: Streamlit-based user interface
2. **Backend**: FastAPI server handling query processing
3. **Database**: SQLite database with mock business data

## 📊 Database Schema

The database includes four main tables:
- **Departments**: department_id, name
- **Products**: product_id, name, category
- **Customers**: customer_id, name, age, region
- **Sales**: order_id, product_id, quantity, price, date, department_id

## 🚀 Getting Started

### Prerequisites
```{python}
$ pip install fastapi uvicorn streamlit pandas requests sqlite3
```

### Running the Application

1. Start the FastAPI backend:
```{python}
$ uvicorn backend:app --reload
```

2. Launch the Streamlit frontend:
```{python}
streamlit run frontend.py
```


3. Access the application at `http://localhost:8501`

## 💡 Usage

1. Enter your query in natural language (e.g., "Show me all sales from the Electronics department")
2. Click "Generate SQL & Fetch Data"
3. View the generated SQL query and results
4. Explore visualizations of the data (when applicable)

## 📝 Example Queries

- "Show all customers from the North region"
- "List total sales by department"
- "Find products with prices above $100"

## 🛠️ Development

The project includes a mock database setup script that:
1. Creates necessary tables
2. Populates them with sample data
3. Establishes relationships between tables

## 🔜 Future Improvements

- Add authentication
- Support more complex queries
- Enhance visualization options
- Add query history