"""Routes for the SQL-DAX-Python Helper application."""
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@main.route('/sql')
def sql_resources():
    """Render the SQL resources page."""
    return render_template('sql.html')


@main.route('/python')
def python_resources():
    """Render the Python resources page."""
    return render_template('python.html')


@main.route('/dax')
def dax_resources():
    """Render the DAX resources page."""
    return render_template('dax.html')
