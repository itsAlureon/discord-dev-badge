<!-- Project Banner -->
<h1 align="center">Create a free Discord Bot</h1>
<p align="center">
  <em>a simple, open-source tutorial on how to unlock the Discord Developer badge.</em>
</p>

---

## Objectives
You’ll learn how to: <br>
-> Create a Discord Bot using the official Developer Portal. <br>
-> Host the bot for free using Replit. <br>
-> Add the bot to your server. <br>
-> Run a /hello command at least once. <br>
-> Qualify for the Active Developer Badge after 24 hours 🎉

---

## 1. Download This Repo

### Download the ZIP
Click the green “Code” button → Download ZIP → to upload files to Replit in the next few steps.

---

## 2. Set Up Your Replit Environment <br>
-> Go to [https://replit.com](https://replit.com) <br>
-> Click “Create Repl” → Choose Python <br>
-> Upload these files: <br>
-> bot.py <br>
-> requirements.txt <br>
-> .env.example (rename this to .env in Replit) <br>

## Install the required libraries: <br>
-> In Replit, go to the “Packages” tab (cube icon) <br>
-> Search and install: discord.py
(or just run: pip install -r requirements.txt in the Shell)

---

## 3. Create Your Discord Bot <br>
-> Go to the Discord Developer Portal
-> Click “New Application” → Name it anything you want (i.e. MyBot)
-> Go to the Bot tab → click “Add Bot”
-> Under “Privileged Gateway Intents,” enable:
Message content (optional)
/Server Members (optional)
-> Copy your Bot Token from the “Bot” tab

---

## 4. Add Your Secrets in Replit <br>
In Replit:
Click the “Secrets” icon (🔐 padlock or .env tab) <br>

Add this environment variable:
```
Key: TOKEN
Value: [Paste your Bot Token here]
```
<br>
Click "Add new secret" to save.

---

## 5. Add Your Bot to Your Discord Server <br>
In the Developer Portal → OAuth2 → URL Generator
Scopes: bot, applications.commands
Bot permissions:
Send Messages
Use Application Commands

Copy the generated URL and paste it in your browser
Choose your server and click “Authorize”

---

## 6. Get Your Guild (Server) ID
In Discord:
Go to User Settings → Advanced → Enable Developer Mode
Right-click your server name → Copy Server ID
Paste that ID in the GUILD_ID = discord.Object(id=...) line inside bot.py (replace the number)

---

## 7. Run the Bot
Click the “Run” button in Replit.

You should see:
Logged in as (YourBotName)
Synced 1 command(s) to guild [YourServerID]


In Discord, type `/hello` — your bot should reply.

---

## 8. Qualify for the Badge

Once the bot is **running and has responded to a slash command**, you’ve done your part.

Now:
- Wait at least 24 hours
- Return to the [Active Developer Badge form](https://discord.com/developers/active-developer)
- Fill it out and confirm eligibility

Done!

---

## 📁 Included Files

| File              | Description                            |
|-------------------|----------------------------------------|
| `bot.py`          | The main bot logic with slash command  |
| `requirements.txt`| Needed libraries (`discord.py`)        |
| `.env.example`    | Template for secret token (rename to `.env`) |
| `README.md`       | This guide                             |

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, fork, or modify it.

---

## Questions?

If you're stuck or have questions, feel free to email me at [gkvyas3@gmail.com].
[https://www.gauravvyas.com]


