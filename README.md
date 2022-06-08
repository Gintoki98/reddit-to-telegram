# reddit-to-telegram
Your reddit feed on telegram, in case you need it

# Preparation
Prepare the next environment variables and run the script

- api_id (The API ID telegram assigns you for your bots)
- api_hash (The API HASH telegram assigns you for your bots)
- bot_token (Your bot's access token)
- channel (the channel's ID EX. -100145579876)
- SUBREDDITS (The subreddits your bot will forward to telegram)
- log (The channel where the bot will send the errors it encounters, same as above)
- CLIENT_ID (The CLIENT ID Reddit assigns you for your bots/apps)
- SECRET (The SECRET Reddit assigns you for your bots/apps)
- username (Your Reddit alias)
- password (Your Reddit Password)
- user_agent (The User Agent that goes in the payload to Reddit)
- SESSION (Telethon .session name)
- YOUR_MESSAGE (The message the bot will display when interacted directly)

# Usage
What this code intends to do is to grab your reddit feed, for now just some specified subreddits and forwards it's media posts (pictures and gifs) to a telegram channel that you must create to display everything
Install the libraries used and run main.py

You can run this project in Railway, the dockerfile is already made to use the script.

# TO-DO
- Forward posts with no media
- Forward posts with videos
- Mode to get your whole reddit feed

# Contact
If you need more explanations you can contact me by hitting me up on telegram at t.me/We_dont_go_to_Ravenholm
