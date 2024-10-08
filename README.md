# Telegram Virtual Phone Number Bot

## Description
This is a **Telegram bot** that provides virtual phone numbers for users using the [5sim.net API](https://5sim.net/). Users can purchase virtual phone numbers for SMS verification across various platforms. Payments are handled through the [Poof.io API](https://poof.io/), allowing users to make payments using Bitcoin, Litecoin, Ethereum, and Solana. The bot generates cryptocurrency QR codes via [bitcoinqrcodemaker.com](https://www.bitcoinqrcodemaker.com/) for easy payment.

The bot is built using the **PyTelegramBotAPI** library and stores user data using **SQLite**. It also includes an admin panel for managing users, balances, and other admins.

## Features
- **Virtual Phone Numbers**: Users can purchase virtual phone numbers for receiving SMS verification codes.
- **Cryptocurrency Payments**: Payments are made via Bitcoin, Litecoin, Ethereum, and Solana using Poof.io.
- **QR Code Generation**: Automatically generates cryptocurrency QR codes for payments.
- **SQLite Database**: Stores user information, balances, transaction history, and admin data.
- **Admin Panel**: Admins can manage user balances, add or remove other admins, and view transactions.
- **Multiple Platforms Supported**: The bot supports purchasing numbers for services like Airbnb, Amazon, Facebook, Instagram, WhatsApp, and many more.

## Tech Stack
- **Telegram Bot API**: Built with the `PyTelegramBotAPI` library.
- **SQLite**: For storing user data, balances, and admin information.
- **5sim.net API**: Provides virtual phone numbers.
- **Poof.io API**: Handles cryptocurrency payments.
- **Bitcoin QR Code Maker**: Generates QR codes for crypto payments.

## Installation

### Requirements
- Python 3.x
- `telebot` library (PyTelegramBotAPI)
- `requests` library
- SQLite database (`sqlite3` module)

### Libraries Installation
To install the required libraries, run:

```bash
pip install pytelegrambotapi requests

## Clone the Repository
Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/breezdev-username/telegram-virtual-phone-bot](https://github.com/BreezDev/E-Sim-Telegram-Bot.git
cd E-Sim-Telegram-Bot

## Database Setup
Ensure that the SQLite database (`US.db`) is set up with the required tables. You can modify or initialize the database in the `dbase.py` file if needed.

## Configure API Tokens
Update the following tokens in the bot script:

- **Telegram Bot Token**: Get this from [BotFather](https://t.me/BotFather).
- **5sim.net API Token**: Get this from your [5sim.net account](https://5sim.net/).
- **Poof.io API Token**: Get this from your [Poof.io account](https://poof.io/).

Place these tokens inside the bot script where indicated:

```python
bot = telebot.TeleBot("bot-token-here")
token = "yourtokenfrom5sim.net"
poof_id = "yourapitokenfrompoof.io"

## Usage

### User Commands
- `/start` - Starts the bot and shows the main menu, including options to top up balance, buy numbers, and check purchase history.

### Admin Commands
- **Admin Panel** - If a user is an admin, they can access the admin panel to:
  - Add or subtract balance from users.
  - Add or remove other admins.
  
Admins are determined based on entries in the `Admindata` table in the SQLite database.

## Payment Process
Users can top up their balance using cryptocurrency. The bot generates a QR code for payment, and users can check their payment status. Once confirmed, the balance is updated in the database.

## Admin Panel Features
- **Add/Subtract Balance**: Admins can add or subtract balance from any user using their user ID.
- **Add/Remove Admins**: Admins can add or remove other admins using their user ID.

## Example Flow
1. A user selects "Buy Number" from the menu.
2. The bot checks the user's balance.
3. If the balance is sufficient, the bot provides a list of platforms (e.g., Amazon, WhatsApp).
4. After selecting a platform, the bot purchases the virtual number and sends it to the user.
5. The user sends an SMS code to the purchased number and retrieves it using the bot.

## Database Structure
The bot uses an SQLite database to manage:
- **UserData Table**: Stores user information, balance, phone numbers, and various options.
- **AdminData Table**: Stores admin user IDs.
- **Transactions Table**: Logs all transactions by users.

