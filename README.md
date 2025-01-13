# Django Telegram Bot with PostgreSQL

## Description

This project demonstrates the integration of a Telegram bot with a Django backend. The bot is designed to handle user interactions efficiently, while Django provides a robust framework for managing the backend. PostgreSQL is utilized as the database to store and manage data effectively.

---

## Features

- Django-based backend framework.
- Telegram bot integration using the Telegram Bot API.
- PostgreSQL database for data storage.
- Scalable and maintainable project architecture.

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/MrTorabekov/django-postgres.git
```

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```env
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
DATABASE_NAME=your-db-name
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### Step 5: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Start the Server

```bash
python manage.py runserver
```

### Step 7: Run the Telegram Bot

If the bot logic is in a separate script, ensure the bot token is configured, and execute the bot script.



---



---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

If you have any questions, feel free to reach out:

- **Email:** diyorbektorabekov22@gmail.com
- **GitHub:** [MrTorabekov](https://github.com/MrTorabekov)

