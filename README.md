# Email Tool

A Python-based email automation tool for sending emails with attachments, CC lists, and logging functionality. This tool is modular and easy to configure for various use cases.

## Features

- Send emails to multiple recipients.
- Attach files to emails.
- Add CC recipients.
- Log email statuses (success, error, invalid email).
- Modular design for easy maintenance and extension.

## Project Structure

```
Email Tool/
├── emailer.py                # Main script to execute the emailer tool
├── modules/
│   ├── email_utils.py        # Utility functions for email handling
│   ├── smtp_utils.py         # Utility functions for SMTP server setup
├── receipient_list.txt       # List of recipient email addresses
├── cc_list.txt               # List of CC email addresses
├── subject.txt               # Email subject
├── body.txt                  # Email body
├── log.csv                   # Log file for email statuses
```

## Prerequisites

- Python 3.6 or higher
- Required Python libraries:
  - `smtplib`
  - `email`
  - `os`
  - `re`
  - `datetime`
  - `time`

## Setup

1. Clone the repository:

   ```shell
   git clone <repository-url>
   cd Email Tool
   ```

2. Configure the following files:
   - `receipient_list.txt`: Add recipient email addresses (one per line).
   - `cc_list.txt`: Add CC email addresses (one per line).
   - `subject.txt`: Add the email subject.
   - `body.txt`: Add the email body content.

3. Update the `emailer.py` script:
   - Set the `sender` email address and `password` in the global variables section.
   - Add file paths for attachments in the `attachment_file_paths` list.

## Usage

1. Run the script:

   ```shell
   python emailer.py
   ```

2. The script will:
   - Validate the sender email address.
   - Check for required files (recipients, CC list, subject, body, log).
   - Send emails to all valid recipients.
   - Log the status of each email in `log.csv`.

## Logging

The `log.csv` file records the status of each email with the following columns:\

- `Recipient`: The recipient's email address.
- `Status`: `success`, `error`, or `invalid`.
- `DateTime`: The timestamp of the email attempt.
- `Error`: The error message (if any).

## Modular Design

The project is divided into modules for better maintainability:

- `email_utils.py`: Contains functions for sending emails and validating email addresses.
- `smtp_utils.py`: Contains functions for setting up the SMTP server.

## Notes

- If using Gmail, ensure you have enabled "App Passwords" for authentication. Refer to [Google's App Passwords Guide](https://myaccount.google.com/apppasswords).
- The script pauses for 5 seconds between sending emails to avoid rate-limiting issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
