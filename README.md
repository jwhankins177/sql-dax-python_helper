# sql-dax-python_helper
A web app to support learners of SQL, Python, and DAX.

## Features

- **SQL Resources**: Learn database querying with SQL tutorials and examples
- **Python Resources**: Master Python programming from basics to advanced concepts
- **DAX Resources**: Understand Data Analysis Expressions for Power BI

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jwhankins177/sql-dax-python_helper.git
   cd sql-dax-python_helper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the development server:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
sql-dax-python_helper/
├── app/
│   ├── __init__.py          # Application factory
│   ├── routes.py            # URL routes and views
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── sql.html
│   │   ├── python.html
│   │   └── dax.html
│   └── static/              # Static files (CSS, JS, images)
│       ├── css/
│       ├── js/
│       └── images/
├── config.py                # Configuration settings
├── run.py                   # Application entry point
└── requirements.txt         # Python dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
