# Resume Extractor

The **Resume Extractor** is a Python script that enables you to search for specific keywords within a collection of resumes stored as PDF files. This tool is designed to help streamline the process of identifying resumes that align with specific skills or qualifications.


## Introduction

When dealing with a large number of resumes, it can be time-consuming to manually review each one to find candidates with specific skills. The **Resume Extractor** script automates this process by allowing you to specify keywords, searching through the resumes, and presenting a list of matching resumes along with the corresponding keywords.

## Features

- Search for multiple keywords within resumes.
- Display detailed information about matching resumes.
- User-friendly command line interface.
- Case-insensitive keyword search.

## Usage

### Requirements

- Python 3.x

### Installation

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `resumeExtractor.py` script.
4. Install any required packages using `pip` if necessary:

### Command Line Interface

To use the script, open a terminal or command prompt and navigate to the directory containing the `resumeExtractor.py` script. Run the script using the following command format:

```bash
python resumeExtractor.py -k KEYWORDS -p FILES_PATH
```

### Example
Suppose you have a directory named demo_resumes/ containing various resumes in PDF format.
You want to search for resumes containing keywords "python" and "js". Run the following command:

```bash
$ py resumeExtractor.py -k "python,js" -p demo_resumes/

***Following are shortlisted resumes.***

1. Filename: Resume1.pdf,
Matching keywords: python, js

2. Filename: Resume2.pdf,
Matching keywords: python, js

3. Filename: Resume3.pdf,
Matching keywords: python

4. Filename: Resume4.pdf,
Matching keywords: js

$ py test_resumeExtractor.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

```

### License
This project is licensed under the MIT License.
