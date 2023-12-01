Theme Preferences Flask App

This is a basic Flask web application that allows users to set and view theme preferences. The theme preferences are stored in cookies and are serialized and deserialized using the pickle module.
Installation

    Clone the repository to your local machine:

    bash

git clone https://github.com/HichamBerbache/insecure-deserialization.git

Navigate to the project directory:

bash

cd insecure-deserialization

Install the required dependencies (Flask):

bash

    pip install Flask

Usage

    Run the Flask application:

    bash

    python app.py

    Open your web browser and go to http://localhost:5000.

    The home page displays the current theme preference. You can click on the "Set Light Theme" or "Set Dark Theme" links to change the theme preference.

Cookie Serialization

The app uses the pickle module to serialize and deserialize the theme preferences before storing and retrieving them from cookies. This is done to demonstrate a basic usage of serialization in a Flask app.

Note: In a real-world scenario, using pickle for serialization can have security implications. Always be cautious when dealing with user input and consider using safer serialization formats.
Contributing

If you find any issues or have improvements to suggest, please feel free to open an issue or create a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
