# Reddit Joke Bot 🤖

A simple Python Reddit bot that monitors comments for the `!joke` trigger and responds with Chuck Norris jokes from an external API.

## Features

- 🎯 **Automatic Response**: Monitors r/test for comments containing `!joke`
- 🃏 **Chuck Norris Jokes**: Fetches random jokes from the Chuck Norris API
- 🔄 **Duplicate Prevention**: Tracks replied comments to avoid spam
- 📝 **Persistent Storage**: Saves processed comment IDs to a text file
- 🔄 **Continuous Monitoring**: Runs in a loop with configurable delays
- 🛡️ **Basic Error Handling**: Handles API failures with fallback messages

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/reddit-joke-bot.git
cd reddit-joke-bot
```

2. Install required dependencies:
```bash
pip install praw requests
```

3. Set up your Reddit API credentials in `config.py` (see [Configuration](#configuration))

## Configuration

Edit `config.py` file in the project with your Reddit API credentials:

```python
# Reddit API credentials
username = "your_reddit_username"
password = "your_reddit_password"
client_id = "your_client_id"
client_secret = "your_client_secret"
```

### Getting Reddit API Credentials

1. Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Choose "script" as the app type
4. Fill in the required fields:
   - **Name**: Your bot's name
   - **Description**: Brief description of your bot
   - **About URL**: Your GitHub repo URL (optional)
   - **Redirect URI**: `http://localhost:8080` (required but not used)
5. Note down your `client_id` (under the app name) and `client_secret`

## Usage

Simply run the bot:

```bash
python your_bot_file.py
```

The bot will:
1. Log into Reddit using your credentials
2. Monitor r/test for new comments every 10 seconds
3. Reply to any comment containing `!joke` with a Chuck Norris joke
4. Save processed comment IDs to avoid duplicate replies

## How It Works

1. **Authentication**: Uses PRAW to authenticate with Reddit
2. **Monitoring**: Checks the latest 25 comments in r/test every 10 seconds
3. **Detection**: Looks for comments containing `!joke` (case-insensitive)
4. **API Call**: Fetches a random Chuck Norris joke from `api.icndb.com`
5. **Response**: Posts the joke as a reply to the original comment
6. **Tracking**: Saves comment IDs to `comment_replied_to.txt` to prevent duplicates

## Example Interaction

**User comment:**
> "I'm bored, someone tell me a !joke"

**Bot response:**
> You requested a Chuck Norris !joke. Here it is:
> 
> > Chuck Norris can divide by zero.

## Project Structure

```
reddit-joke-bot/
├── your_bot_file.py           # Main bot code
├── config.py                  # Reddit API credentials
├── comment_replied_to.txt     # Processed comments (auto-created)
└── README.md                  # This file
```

## Dependencies

- `praw` - Python Reddit API Wrapper
- `requests` - HTTP library for Chuck Norris API calls
- `python>=3.6` - Required Python version

## Configuration Options

You can modify these settings directly in the code:

- **Subreddit**: Currently set to `r/test` (line with `reddit.subreddit('test')`)
- **Trigger phrase**: Currently `!joke` (case-insensitive)
- **Comment limit**: Checks latest 25 comments per cycle
- **Sleep interval**: 10 seconds between checks
- **API endpoint**: Chuck Norris jokes from `api.icndb.com`

## Error Handling

The bot includes basic error handling for:
- **API failures**: Shows fallback message if Chuck Norris API is unavailable
- **Reply errors**: Logs failed reply attempts
- **Network timeouts**: 5-second timeout on API requests

## Important Notes

⚠️ **Security**: 
- Add `config.py` to your `.gitignore` file to avoid committing credentials
- Never share your Reddit API credentials publicly

⚠️ **Reddit Guidelines**:
- This bot is designed for r/test (a testing subreddit)
- Follow Reddit's [API Terms of Use](https://www.reddit.com/wiki/api-terms)
- Be respectful and don't spam other subreddits
- Some subreddits prohibit bots

## Troubleshooting

### Common Issues

**"Logging in..." but never connects:**
- Check your Reddit credentials in `config.py`
- Ensure your Reddit account has sufficient karma
- Verify client_id and client_secret are correct

**Bot replies to old comments after restart:**
- The current version resets the tracking on restart
- Comment IDs are loaded but not used (known bug)

**API errors:**
- Chuck Norris API occasionally goes down
- Bot will show fallback error message in these cases

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify your Reddit API credentials
3. Test in r/test subreddit first
4. Open an issue on GitHub with error details

## License

This project is licensed under the MIT License.

## Disclaimer

This bot is for educational purposes. Always follow Reddit's terms of service and subreddit rules. Test responsibly in appropriate subreddits like r/test before deploying elsewhere.

## Future Improvements

Potential enhancements for future versions:
- Better logging system
- Configuration file for settings
- Database storage instead of text file
- Multiple joke sources
- Graceful shutdown handling
- Rate limiting improvements
