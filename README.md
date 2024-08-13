# ARQAN: Automated Requirements Analysis Tool

ARQAN is a powerful Streamlit-based application frontend designed to assist in analyzing and extracting security requirements from various sources. The app features multiple tools tailored for different aspects of security requirements management.

## Features

1. **STIG Search**: 
   - **Description**: Search for relevant Security Technology Implementation Guidelines (STIG) based on a given textual security requirement and platform (e.g., Windows 10). The tool provides detailed security guidelines or even specific fixes.
   - **Use Case**: Ideal for security professionals seeking quick and accurate STIG recommendations tailored to their specific platforms and requirements.

2. **Security Requirements Extraction**: 
   - **Description**: Upload a PDF file, and this tool will analyze the document to extract security-related requirements automatically.
   - **Use Case**: Perfect for analyzing lengthy documents to quickly identify and extract crucial security requirements.

## Installation

To run the ARQAN app locally, you'll need to use [Poetry](https://python-poetry.org/) for dependency management. Follow the steps below to set up and run the app:

### Prerequisites

- Python 3.11 or higher
- Poetry installed

### Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/VeriDevOps/arqan.front-steamlit
    cd arqan.front-steamlit
    ```

2. **Install Dependencies**:
    ```bash
    poetry install
    ```

3. **Run the Streamlit App**:
    ```bash
    poetry run streamlit run ./app/ARQAN.py
    ```

## Usage

Once the app is running, open your browser and navigate to `http://localhost:8501`. You will be greeted with the home page, where you can explore the available tools:

- **STIG Search**: Enter the textual security requirement and select the platform to search for relevant STIGs.
- **Security Requirements Extraction**: Upload a PDF document to extract security requirements.

## Limitations

- Use any available username. You can set your own password on the first login.
- The app uses a remote backend for running NLP operations with various models.
- The models are prototypical and under construction, so the results may be suboptimal.

## More information

For more information about applied techniques please check our paper:

- Natural Language Processing with Machine Learning for Security Requirements Analysis: Practical Approaches, available at [Springer](https://www.springerprofessional.de/en/natural-language-processing-with-machine-learning-for-security-r/26534462) or at [ResearchGate](https://www.researchgate.net/publication/376568438_Natural_Language_Processing_with_Machine_Learning_for_Security_Requirements_Analysis_Practical_Approaches)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the APACHE 2.0 License. See the `LICENSE` file for details.