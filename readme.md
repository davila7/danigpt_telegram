# Telegram DaniGPT bot with CodeGPT

This is a Telegram chatbot that uses CodeGPT to generate responses. It allows you to interact with DaniGPT by sending messages to it.

## Prerequisites

Before running the code, make sure you have the following:

- Python 3 installed
- `streamlit`, `telebot`, `requests`, and `dotenv` libraries installed
- A Telegram API key and CodeGPT API key

Create an account in CodeGPT Plus in this link: https://account.codegpt.co

## Installation

Clone the repository:

```bash
git clone https://github.com/davila7/danigpt_telegram.git
```

### Install the required libraries:

```bash
pip install -r requirements.txt
```

Set up environment variables:
Create a .env file in the root directory of your project.

Add the following lines to the .env file:

- TELEGRAM_KEY=your-telegram-api-key
- CODEGPT_API_KEY=your-codegpt-api-key
- CODEGPT_AGENT_ID=your-codegpt-agent-id

## Run the code:

```bash
streamlit run app.py
```

## Usage
- Start the bot by running the code.
- Open your Telegram app and search for the bot.
- Send messages to the bot and it will generate responses using CodeGPT.

## License
This project is licensed under the MIT License - see the LICENSE file for details.