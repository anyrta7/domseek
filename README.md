# DomSeek Project v0.1

## Table of Contents
- [DomSeek Project v0.1](#domseek-project-v01)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Basic Usage](#basic-usage)
    - [Advanced Options](#advanced-options)
    - [Examples](#examples)
  - [Output Details](#output-details)
  - [Project Structure](#project-structure)
  - [License](#license)

---

## Introduction
**DomSeek** is a Python-based command-line utility designed to evaluate the status of multiple domains or URLs provided via a file or standard input. This tool is optimized for performance, flexibility, and extensibility, making it suitable for both personal and professional use.

## Features
- **Multi-threaded processing** for faster execution.
- **Customizable status code filters**, allowing users to focus on specific HTTP responses.
- Support for **standard input (stdin)** and file-based input.
- **Domain filtering** by keywords or patterns.
- **Color-coded output** using `colorama` for better readability.
- Handles URLs without protocols (e.g., `example.com`).
- Distinguishes between active and inactive domains with detailed reporting.

## Requirements
- Python 3.8 or higher
- Required Python packages:
  - `requests`
  - `colorama`
  - `argparse`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anyrta7/domseek.git
   cd domseek
   ```

2. Install dependencies:
   
   using virtual environment (optional but recomended)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

    without virtual environment
   ```bash
   pip install -r requirements.txt
   ```

3. Make the script executable (optional):
   ```bash
   chmod +x main.py
   ```

## Usage

### Basic Usage
To check domains listed in a file and filter by specific status codes:
```bash
python main.py -l list.txt -sc 200
```

To pipe a list of domains via standard input:
```bash
cat list.txt | python main.py -sc 200
```

### Advanced Options
- `-sc`, `--status-code`: Filter by HTTP status codes (comma-separated).
- `-fd`, `--filter-domain`: Filter domains by specific substrings or keywords (comma-separated).
- `-ia`,  `--inactive`: Display only inactive domains.
- `-is`, `--ignore-ssl`: Ignore SSL certificate validation errors.
- `-th`, `--threads`: Set the number of threads for parallel processing (default: 10).
- `-tm`, `--timeout`: Set the timeout for HTTP requests (default: 5 seconds).
- `--retry`: Number of retries for failed requests (default: 3).

### Examples
1. Check domains and display only those responding with 200 or 403:
   ```bash
   python main.py -l domains.txt -sc 200,403
   ```

2. Filter domains containing specific keywords:
   ```bash
   python main.py -l domains.txt --filter "example,site"
   ```

3. Process domains with 20 threads:
   ```bash
   python main.py -l domains.txt -th 20
   ```

## Output Details
- **Active Domains:** Displayed as `[status code] domain`
- **Inactive Domains:** Displayed as `[INACTIVE] domain`
- **Color Coding:**
  - Green: Active domains with valid status codes.
  - Yellow: Warnings or retries.
  - Red: Errors or inactive domains.

## Project Structure
```
project_root/
├── main.py             # Main script
├── requirements.txt    # Python dependencies
├── utils/
│   └── file_handler.py # File handler 
├── domain_checker/
│   ├── filters.py      # Domain filters
│   └── checker.py      # Core
└── README.md           # Documentation
```
 tests/
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push to your fork:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

