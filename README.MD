# Job Search Engine Application

This Streamlit application provides a simple and interactive way to search for jobs using the SERPAPI Google Jobs Search API. Users can input their desired job title and location, and the app will display a list of available jobs matching the criteria.

## Features

- **User-Friendly Interface:** Easy to use text inputs for job title and location.
- **Dynamic Job Search:** Leverages the SERPAPI to fetch and display job listings.
- **Interactive Results:** Displays job details in an expandable format for each listing.

## Prerequisites

Before running this application, you'll need:

- Python 3.6 or newer
- Streamlit
- An API key for SERPAPI

## Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <repository-path>

## Install dependencies

### Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate 
```

### Install the required packages:

```bash
pip install streamlit serpapi
```

## Configure API Key

Sign up for an API key at SERPAPI.

Create a .streamlit/secrets.toml file in your project directory.

### Add your API key to the secrets.toml file:

toml
api_key = "YOUR_SERPAPI_API_KEY"

## Running the Application
To run the application, execute the following command in your terminal:

```bash
streamlit run job_engine_app.py
```


## Usage
Starting the App: Open the provided URL in your web browser after running the command above.
Searching for Jobs: Enter the desired job title and location in the input fields and click "Search Jobs" to see the results.

## License
MIT

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

# job-engine
# index-job-engine
