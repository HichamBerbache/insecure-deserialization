# Theme Preferences Flask App

This is a basic Flask web application that allows users to set and view theme preferences. The theme preferences are stored in cookies and are serialized and deserialized using the `pickle` module.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/HichamBerbache/insecure-deserialization.git
    ```

2. Navigate to the project directory:

    ```bash
    cd insecure-deserialization
    ```

3. Install the required dependencies (Flask):

    ```bash
    pip install Flask
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

3. The home page displays the current theme preference. You can click on the "Set Light Theme" or "Set Dark Theme" links to change the theme preference.



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
