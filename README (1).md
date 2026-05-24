# Password Hashing Authentication System

A simple Python-based authentication program that demonstrates secure password hashing and verification using the `bcrypt` library.

## Features

- Secure password hashing with salt
- Password verification using `bcrypt.checkpw()`
- Command-line interface
- Beginner-friendly Python project
- Demonstrates basic authentication workflow

## Technologies Used

- Python 3
- `bcrypt` library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-hash-authentication.git
```

2. Navigate to the project folder:

```bash
cd password-hash-authentication
```

3. Install required dependency:

```bash
python -m pip install bcrypt
```

## Usage

Run the Python script:

```bash
python main.py
```

## Program Menu

```text
1. Generate salt hash and check password
2. Exit Program
```

### Example Output

```text
1. Generate salt hash and check password
2. Exit Program

Choose a option: 1
Enter your username: admin
Enter your password: mypassword

The salted hash is:
b'$2b$12$...'

Re-enter the password to check: mypassword
Login success
```

## Project Structure

```text
password-hash-authentication/
│
├── main.py
├── README.md
└── requirements.txt
```

## Requirements

Create a `requirements.txt` file and add:

```text
bcrypt
```

Install using:

```bash
pip install -r requirements.txt
```

## Learning Objectives

This project helps understand:

- Password hashing
- Salting passwords
- Secure authentication basics
- Using external Python libraries
- Input handling in Python

## Security Note

This project is for educational purposes only.

In real-world applications:

- Never store plain-text passwords
- Use secure databases
- Implement proper user management
- Add rate limiting and security protections

## License

This project is open-source and available under the MIT License.
