# Discord Bot

This project is a simple Discord bot built using Python. It serves as a template for creating your own bot with customizable commands and utilities.

## Project Structure

```
discord-bot
├── bot
│   ├── __init__.py
│   ├── main.py
│   ├── commands
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── README.md
└── .env
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd discord-bot
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

## Usage

To run the bot, execute the following command:
```
python bot/main.py
```

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.