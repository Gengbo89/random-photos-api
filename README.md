# Random Photos API

This project is a simple Flask application that serves random images from a local directory. It provides an API endpoint to retrieve a random photo from the specified folder.

## Project Structure

```
random-photos-api
├── src
│   ├── main.py          # Entry point of the application
│   ├── api
│   │   └── photos.py    # API for handling photo requests
│   └── utils
│       └── file_utils.py # Utility functions for file handling
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd random-photos-api
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

The application will start and listen for requests. You can access the random photo API at:
```
http://localhost:5000/api/random-photo
```

## License

This project is licensed under the MIT License.