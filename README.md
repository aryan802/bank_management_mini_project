# Bank Management System (Python)

A simple command-line Bank Management System built using Python, Object-Oriented Programming (OOP), and File Handling.

## Features

- Create and access bank accounts
- Deposit money
- Withdraw money
- Check account balance
- Persistent balance storage using text files
- Individual transaction logs for each user
- Automatic timestamping of all account activities

## Project Structure

```
bank/
│
├── balances.txt
├── logs/
│   ├── Ramesh.log
│   ├── Suresh.log
│   └── ...
│
└── main.py
```

## Storage Mechanism

### balances.txt

Stores account balances in the format:

```
Ramesh,800
Suresh,1500
Mohan,300
```

### User Log Files

Each user has a dedicated log file inside the `logs` folder.

Example: `logs/Ramesh.log`

```
2026-05-31 10:12:01 - Account Created
2026-05-31 10:15:33 - Deposited 1000
2026-05-31 10:18:04 - Withdrawn 200
```

## Concepts Used

### Object-Oriented Programming (OOP)

- Classes
- Objects
- Constructors (`__init__`)
- Instance Attributes
- Methods

### File Handling

- Reading files
- Writing files
- Appending data
- Managing persistent storage

### Python Modules

- `datetime`
- `os` (optional)

## How It Works

### Account Access

1. The system searches for the user in `balances.txt`.
2. Existing balance is loaded.
3. Activity is recorded in the user's log file.

### Deposit

1. Balance is increased.
2. Updated balance is written to `balances.txt`.
3. Transaction is logged with timestamp.

### Withdrawal

1. Balance availability is checked.
2. Amount is deducted if sufficient funds exist.
3. Updated balance is saved.
4. Transaction is logged.

## Sample Run

```
Welcome to Bank Management System

1. Deposit
2. Withdraw
3. Check Balance

Enter choice: 1
Enter amount: 1000

Successfully Deposited
```

## Future Improvements

- Money Transfer Between Accounts
- Account Creation Interface
- Account Deletion
- Transaction History Viewer
- PIN-Based Authentication
- Account Number Generation
- Interest Calculation
- CSV/JSON Storage
- SQLite Database Integration
- Graphical User Interface (GUI)

## Learning Outcomes

This project demonstrates practical usage of:

- Python OOP
- File Handling
- Data Persistence
- Transaction Logging
- Basic System Design

It serves as a beginner-friendly project for students learning Python development and backend fundamentals.

## Author

Aryan Jain

Built as a learning project to practice Python OOP and File Handling.
