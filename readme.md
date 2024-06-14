# PDF Password Brute Force Tool

This tool allows you to unlock password-protected PDF files by brute-forcing the password. The application is built with Python and Flask, providing a web interface for easy interaction.

## Features

- Upload a PDF file to unlock
- Specify the type and length of the password
- Display the estimated time required to process
- Download the unlocked PDF file once processed
- User-friendly web interface

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/unlockpdf.git
    cd unlockpdf
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to**:

    ```
    http://127.0.0.1:5000/
    ```

3. **Upload your PDF file**:

    - Choose the PDF file you want to unlock.

4. **Specify the password characteristics**:

    - **Number of characters in password**: Enter the maximum length of the password.
    - **Type of characters in password**: Choose from Numbers, Alphabets, or Alphanumeric.

5. **Start the brute force process**:

    - Click on the "Start Brute Force" button.
    - The application will display a processing message and the estimated time to process the file.

6. **Download the unlocked PDF**:

    - Once the password is found, the application will display the password and provide a download link for the unlocked PDF.

## Estimated Processing Time

The time required to process the file depends on the length and complexity of the password:

- **Short numeric passwords (1-4 characters)**: Typically a few seconds to a minute.
- **Longer numeric or simple alphabetic passwords (5-6 characters)**: May take several minutes.
- **Complex alphanumeric passwords or passwords longer than 6 characters**: Could take a significant amount of time, ranging from minutes to hours.

Please be patient while the tool processes the file. The application will keep you informed about the estimated time and the status of the process.

## Project Structure

unlockpdf/
├── app.py # Flask application
├── templates/
│ └── index.html # HTML template
├── static/
│ ├── css/
│ │ └── style.css # CSS file for styling
│ └── js/
│ └── script.js # JavaScript file for interactivity
├── uploads/ # Directory for uploaded and processed files
├── venv/ # Virtual environment (optional)
└── README.md # Project README file


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [trivedi.gaurav30@gamil.com](mailto:trivedi.gaurav30@gamil.com).

---

Enjoy using the PDF Password Brute Force Tool!