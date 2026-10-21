# Employee Profile Validator

A Python project that practices cleaning and validating employee data using built-in string methods. Built as part of the freeCodeCamp Python curriculum.

## What it does

- Extracts a username from an email address
- Checks emails for required parts (`@`, `.com`)
- Cleans messy names and emails (whitespace and capitalization)
- Generates a display name and a name badge from an email
- Removes dashes from phone numbers
- Splits and rejoins addresses
- Validates an employee code prefix (`EMP`) and email ending
- Counts characters such as dots and dashes

## String methods used

`find()`, `strip()`, `lower()`, `upper()`, `title()`, `replace()`, `split()`, `join()`, `startswith()`, `endswith()`, `count()`, string slicing, the `in` operator, and f-strings.

## How to run

Requires Python 3.

```bash
python3 main.py
```

## Example output

```
Email: alice.johnson@company.com
Position of @: 13
Username: alice.johnson
Has @ symbol: True
Has .com: True
Cleaned name: 'Sarah Davis'
Display name: Sarah Davis
Starts with EMP: True
```

## What I learned

- Cleaning inconsistent user input with `strip()`, `lower()`, and `title()`
- Slicing strings using positions found with `find()`
- Combining string methods to validate and transform data

## Credits

Built following the freeCodeCamp Python curriculum.

## Author

Trevor Maringa
[GitHub](https://github.com/Trevor566) | [LinkedIn](https://linkedin.com/in/trevor-maringa-143958284)
