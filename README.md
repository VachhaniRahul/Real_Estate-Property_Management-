<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Real Estate Management System</h1>
    <h2>Description</h2>
    <p>
        The <strong>Real Estate Management System</strong> is a Django web application designed to help real estate agents and property managers manage properties, clients, and transactions efficiently. This system allows users to:
    </p>
    <ul>
        <li>View and manage property listings</li>
        <li>Register and manage clients</li>
        <li>Track property transactions and status</li>
        <li>Search and filter properties based on various criteria</li>
    </ul>
    <p>
        The project uses <strong>Bootstrap</strong> for a responsive and modern UI, and <strong>Django</strong> for backend operations.
    </p>
    <h2>Features</h2>
    <ul>
        <li><strong>Property Listings:</strong> View all properties with details such as price, location, size, and type.</li>
        <li><strong>Add Property:</strong> Add new properties to the system with details like price, location, size, and type.</li>
        <li><strong>Client Management:</strong> Register and manage client information, including contact details and property interests.</li>
        <li><strong>Search and Filter:</strong> Search for properties based on criteria like location, price range, and property type.</li>
        <li><strong>Transaction Tracking:</strong> Keep track of property transactions and their current status.</li>
    </ul>
    <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Django</li>
        <li><strong>Frontend:</strong> HTML5, CSS3, Bootstrap 5</li>
        <li><strong>Database:</strong> SQLite (Django default)</li>
    </ul>
    <h2>Requirements</h2>
    <p>To run this project locally, make sure you have the following installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Django 5.x</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/VachhaniRahul/Real_Estate-Property_Management-</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd real-estate-management</code></pre>
        </li>
        <li>Create a virtual environment:
            <pre><code>python -m venv env</code></pre>
        </li>
        <li>Activate the virtual environment:
            <ul>
                <li>On Windows:
                    <pre><code>.\env\Scripts\activate</code></pre>
                </li>
                <li>On macOS/Linux:
                    <pre><code>source env/bin/activate</code></pre>
                </li>
            </ul>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run migrations to set up the database:
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li>Start the development server:
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li>Open your browser and go to:
            <pre><code>http://127.0.0.1:8000/</code></pre>
        </li>
    </ol>
    <h2>Usage</h2>
    <h3>Viewing Properties</h3>
    <ul>
        <li>Click on the "View Properties" link to see a list of all available properties.</li>
        <li>Details such as price, location, and size will be displayed in a table format.</li>
    </ul>
    <h3>Adding a Property</h3>
    <ul>
        <li>Click on "Add Property" to open a form.</li>
        <li>Fill in the property details and click <strong>Submit</strong> to add the property to the database.</li>
    </ul>
    <h3>Managing Clients</h3>
    <ul>
        <li>Click on "Manage Clients" to view and update client information.</li>
    </ul>
    <h3>Searching for Properties</h3>
    <ul>
        <li>Use the search bar and filters to find properties based on location, price range, and type.</li>
    </ul>
    <h2>Future Improvements</h2>
    <ul>
        <li>Add user authentication and authorization.</li>
        <li>Integrate a payment gateway for property transactions.</li>
        <li>Include property images and virtual tours.</li>
        <li>Enhance search functionality with advanced filters.</li>
    </ul>
    <h2>License</h2>
    <p>
        This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.
    </p>
    <h2>Contributing</h2>
    <p>
        Contributions are welcome! Please submit a pull request or open an issue for any suggestions or bug reports.
    </p>
</body>
</html>
