# random-adventure-generator-tg-bot
Telegram bot for the ["Random adventure generator"](https://github.com/DenisGavar/random-adventure-generator) application

[Try it](https://t.me/RandomAdventureGeneratorBot)

List of Available Telegram Bot Commands:

    -/start: Registers a new user in the database via the API.

    -/generate_task [category]: Generates a random task, optionally filtered by category, using the Random Adventure Generator API.

    -/get_task [category]: Gets an existing random task, optionally filtered by category.

    -/tasks [status]: Lists all tasks associated with the user, optionally filtered by status (assigned|completed).

    -/complete_task [task_id]: Marks a specified task as completed.

    -/categories: Displays a list of available categories for generating tasks.