# Scratch Bot Template for Command Responses

This template demonstrates how to create a Scratch bot that listens for specific commands in a studio's comment section and replies with a response. You can easily customize this bot by adding your own commands to fit your needs.

## Requirements

- **Python 3.x**: Make sure you have Python installed on your system.
- **scratchattach**: This Python library is used to interact with Scratch. Install it using pip:

    pip install scratchattach

## Setup

1. **Install dependencies**:
    Make sure you have `scratchattach` installed. Run the following command in your terminal or command prompt:

    pip install scratchattach

2. **Replace credentials**:
    In the script, replace the `"username"` and `"password"` in the login function with your Scratch account credentials.

    ```python
    session = sa.login("username", "password")
    ```

3. **Replace studio ID**:
    Replace the `"studioid"` with the ID of your studio, where the bot will be active and responding to comments.

    ```python
    studio = session.connect_studio("studioid")
    ```

## Customizing Commands

You can easily add your own commands by editing the `commands` dictionary. Each key represents a command that users can type in the comments, and the corresponding value is the response the bot will give.

Example:
```python
commands = {
    "/example1": lambda: f"this is an example command (RNTAS: {random.randint(1000, 9999)})",
}
```

You can define as many commands as you like by adding new key-value pairs to the `commands` dictionary.

## How It Works

1. **Login**: The bot logs into Scratch using the provided credentials.
2. **Studio Connection**: The bot connects to the studio specified by the studio ID.
3. **Comment Monitoring**: The bot continuously checks for new comments in the studio.
4. **Command Recognition**: If a comment matches a predefined command, the bot will queue a response.
5. **Timed Replies**: Every 30 seconds, the bot replies to the next queued comment, ensuring it doesn't overwhelm the system with too many replies at once.

## Error Handling

The bot includes basic error handling:
- It retries if it fails to retrieve comments or reply.
- It waits 1 second before retrying if an error occurs during the comment retrieval.

## Running the Bot

Once you've set up your credentials and customized the bot as needed, you can run the bot by executing the script:

    python bot.py

## Notes

- The bot works by checking comments in the connected studio and replies to those that contain predefined commands.
- The bot limits its replies to one every 30 seconds to avoid spam and rate limiting.
- You can further modify the bot's behavior and add more advanced features like multiple studios or different types of responses.

