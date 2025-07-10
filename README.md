# Prompt-Based Data Analytics

This repository contains a project that provides an interactive web application for prompt-driven data analysis using Streamlit and pandasai. The application allows users to upload CSV files and perform data queries using natural language prompts powered by OpenAI's language model.

## Project Overview

The goal of this project is to simplify data analysis by enabling users to interact with their data using natural language prompts. The application supports CSV file uploads and provides an intuitive interface for querying and visualizing data.

### Key Features:
- **Prompt-Driven Analysis:** Utilize OpenAI's language model to query and analyze data using natural language prompts.
- **CSV Uploads:** Users can upload their CSV files for analysis.
- **Secure API Management:** Implemented secure management of the OpenAI API key.
- **User-Friendly Interface:** Designed with Streamlit to ensure an intuitive and accessible user experience.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Nik9296/Prompt-Based-Data-Analytics
    cd Prompt_Based_Data_Analytics
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    - Add your API key to the `config.yaml` file or use environment variables for secure management.

## Usage

1. **Running the Application:**

    To start the Streamlit web application, run the following command:
    ```bash
    streamlit run app.py
    ```

2. **Uploading a CSV File:**

    - Open the web application in your browser.
    - Upload a CSV file using the provided interface.
    - Enter natural language prompts to query and analyze the data.
      
**Results**

https://github.com/Nik9296/Prompt-Based-Data-Analytics/blob/main/prompt%20analytics%20result.png

## Project Structure

- `app.py`: Main application file containing the Streamlit app.
- `.env`: file for managing API key securely.
- `requirements.txt`: List of dependencies required to run the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements.

## Contact

For any inquiries, please contact Nikhil Vijay Divekar at nikhildivekar041@gmail.com.
