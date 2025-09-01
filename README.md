<!-- Project Banner -->
<h1 align="center">Create & Run a Free Discord Bot</h1>
<p align="center">
  <em>A simple, open-source tutorial on how to unlock the Discord Developer badge in the easiest way possible.</em>
</p>

<p align="center">
<img width="154" height="86" alt="image" src="https://github.com/user-attachments/assets/5b454916-ad0e-4c1b-b040-334d5332bca9" />
</p>

---

## Objectives
In under 15 minutes, you’ll learn how to: <br><br>
-> Create a Discord Bot using the official [Developer Portal](https://discord.com/developers/active-developer). <br>
-> Host the bot for free using [Replit](https://replit.com/). <br>
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
Click the “Secrets” tab <br>
<img width="117" height="52" alt="image" src="https://github.com/user-attachments/assets/bb64e024-5e93-4eb0-966e-1cf12f67fa5b" />
<br>


Click "+ New Secret" and add the environment variable:
```
Key: TOKEN
Value: [Paste your Bot Token here from Step 3]
```
<br>
Click "Add secret" to save.

<img width="1107" height="54" alt="image" src="https://github.com/user-attachments/assets/74b781c8-f5e8-415c-b431-f4240c89e497" />
<br>

---

## 5. Add Your Bot to Your Discord Server <br>
In the Developer Portal → OAuth2 → URL Generator <br>

Scopes: bot, applications.commands <br>

Bot permissions:
Send Messages
Use Application Commands
<br>

-> Copy the generated URL and paste it in your browser <br>
-> Choose your server and click “Authorize”

---

## 6. Get Your Guild (Server) ID
In Discord:
Go to User Settings → Advanced → Enable Developer Mode
Right-click your server name → Copy Server ID
Paste that ID in the GUILD_ID = discord.Object(id=...) line inside bot.py (replace the number)

---
## 6.5 Check your User Settings

Discord will not be able to read your account for commands until you have "Use data to improve Discord" enabled. <br>
You can enable this in Discord -> User Settings -> Data & Privacy <br>

<img width="1005" height="215" alt="image" src="https://github.com/user-attachments/assets/74554588-fab4-473e-8b6c-b4ab15448337" />

## 7. Run the Bot
Click the “Run” button in Replit. <br>
<img width="97" height="46" alt="image" src="https://github.com/user-attachments/assets/0a3447a7-8a72-4c22-9894-0f3529eaa527" />
<br>

In the Replit Console tab, you should see: <br>
-Logged in as (YourBotName) <br>
-Synced 1 command(s) to guild [YourServerID] <br>

In Discord, you should see your bot online!
<br>

<img width="267" height="161" alt="image" src="https://github.com/user-attachments/assets/dd37922e-b08d-44b7-9b7f-0df54eee5b82" />
<br><br>


In Discord, type `/hello` — your bot should reply.

<img width="302" height="85" alt="image" src="https://github.com/user-attachments/assets/6d019e39-3d73-4311-94f4-9cd8118ff777" />

<br>


---

## 8. Qualify for the Badge

Once the bot is **running and has responded to a slash command**, you’ve done your part.

Now:
- Wait at least 24 hours
- Return to the [Active Developer Badge form](https://discord.com/developers/active-developer)
- Claim your badge

Done!

<img width="792" height="309" alt="image" src="https://github.com/user-attachments/assets/82fd789b-3676-4f3e-8ef1-31640145c879" />


*Note: Remember to run the bot and command at least once every 30 days or Discord will remove the badge. <br>
[Discord Developer - Maintaining Eligibility](https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge?ref=badge#h_01GPP5AFAB3E7PAN374XQD60BP)*

---

## Included Files

| File              | Description                            |
|-------------------|----------------------------------------|
| `bot.py`          | The main bot logic with slash command  |
| `requirements.txt`| Needed libraries (`discord.py`)        |
| `.env.example`    | Template for secret token (rename to `.env`) |
| `README.md`       | This guide                             |

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to do anything with it.

---

## Questions?

If you're stuck or have questions, feel free to email me at [gkvyas3@gmail.com](mailto:gkvyas3@gmail.com). <br>
[https://www.gauravvyas.com](https://www.gauravvyas.com)


