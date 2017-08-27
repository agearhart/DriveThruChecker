# DriveThruChecker
Script used to validate that products on DriveThruRPG have both a Quick and Full preview if they're expected for a list of products

# How to use these scripts

There are 2 ways to use this repository

## 1 Python

[Install Python 2](https://www.python.org/downloads/) on your computer

From a command line run
```
python DriveThruChecker.py Products.json
```

## 2 Docker

[Install Docker](https://docs.docker.com/engine/installation/) and run the following 2 commands from a command like
```
docker build -t drivethruchecker .
docker run -it --rm drivethruchecker
```

# Configuration
To configure the project open Products.json and add new product objects like the example.  The product id comes directly from the URL from your DriveThruRPG product.
