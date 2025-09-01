<!-- Project Banner -->
<h1 align="center">Discord Active Development Badge</h1>
<p align="center">
  <em>A simple, open-source tutorial on how to unlock the Discord Developer badge.</em>
</p>

<p align="center">
<img width="206" height="206" alt="image" src="https://github.com/user-attachments/assets/ea7aca0f-bb48-4977-8bd0-399d79f1fb79" />
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

## 1. Set Up Your Replit Environment <br>
-> Go to [https://replit.com](https://replit.com) <br>
-> Create a free account or login <br>
-> Import Github files to Replit

### Method A (Fastest)

-> Simply input this link into your browser for Replit to automatically import this Github Repository as your own project: <br>
```
https://replit.com/import/github/itsAlureon/discord-dev-badge
```
-> Click "Import from Github"
<br>

<img width="1085" height="572" alt="image" src="https://github.com/user-attachments/assets/7b903767-1fe1-4679-9c0f-6686d15b2750" />
<br>

### Method B
-> Click "Import code or design" on your Replit dashboard <br>
-> Click "Github" <br>
-> Copy and Paste this Github Repo link into the URL section:
```
https://github.com/itsAlureon/discord-dev-badge
```
-> Click "Import from Github" <br>

## After importing, add the run command
-> After you've successfully imported, Replit will ask you for a run command. Type in:
```
python bot.py
```
<img width="458" height="229" alt="image" src="https://github.com/user-attachments/assets/75b52ba5-6d4f-4c62-93c2-a68ebf98bd93" />
<br>
-> Click 'Confirm and Close'
<br><br>


Congrats, your project is now set up. <br><br>

## Now, install the required libraries: <br>
-> In Replit, open a new tab next to Console and Shell. <br>

<img width="389" height="230" alt="image" src="https://github.com/user-attachments/assets/9ccc75a1-dfa7-4fc1-9b17-c2cd6b3b4608" />
<br><br>

-> Search for "Dependencies" or "Packages" to open the dependency importer. <br>
-> Add 'discord.py' and install it. <br>
<img width="1235" height="463" alt="image" src="https://github.com/user-attachments/assets/74fa3206-5cb0-48b2-b3c7-cb83fd6c2c2f" /> 
<br>


---

## 3. Create Your Discord Bot <br>
-> Go to the Discord Developer Portal <br>
-> Click “New Application” <br>
-> Name it anything you want (i.e. MrBot) <br><br>
<img width="441" height="352" alt="image" src="https://github.com/user-attachments/assets/6467315c-c9cc-40e4-8254-78f6b8e1b826" />
<br>

-> Go to the OAuth2 tab on the Developer Portal <br>
-> Reset to generate a 'Client Secret' that will be used as your Bot Token <br>
-> Copy your 'Client Secret' and save it, this is your Bot Token. Do not share this with anyone <br>

<img width="211" height="136" alt="image" src="https://github.com/user-attachments/assets/6bda2966-527b-417d-b66e-067c7af274af" />
<br>


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
Click "Add secret" to save

<img width="1107" height="54" alt="image" src="https://github.com/user-attachments/assets/74b781c8-f5e8-415c-b431-f4240c89e497" />
<br>

---

## 5. Add Your Bot to Your Discord Server <br>

-> In the Developer Portal → OAuth2 → URL Generator <br>

-> Scope Permissions: <br>
(✓) bot <br>
(✓) applications.commands <br>

<img width="720" height="480" alt="image" src="https://github.com/user-attachments/assets/61a3b421-e71c-496f-a1e5-81963eb93484" />
<br><br>

-> Bot Permissions: <br>
(✓) Send Messages <br>
(✓) Use Slash Commands <br>

<img width="720" height="480" alt="image" src="https://github.com/user-attachments/assets/18d40f6d-68f5-4138-a595-8aac118c6abe" />
<br>

-> Copy the 'Generated URL' at the bottom of the page and paste it in your browser <br>
-> Choose your server and click “Authorize” <br><br>

Congrats, now your bot should be in your server!

---

## 6. Get Your Guild (Server) ID <br>
-> In Discord, go to User Settings → Advanced → Enable Developer Mode <br>

<img width="1009" height="547" alt="image" src="https://github.com/user-attachments/assets/69559015-77c0-40ca-9268-a89f4380fb51" />
<br>

-> Right-click your server icon on Discord and "Copy Server ID"
<br>
<img width="163" height="61" alt="image" src="https://github.com/user-attachments/assets/13903a72-ca34-48c1-989a-214016fc8c6d" />
<br>

-> Paste that ID in the GUILD_ID = discord.Object(id=...) line inside the "bot.py" file on Replit (replace the number)
<img width="1176" height="235" alt="image" src="https://github.com/user-attachments/assets/e91b85c1-1fe1-4acd-aecb-0125381622d8" />
<br>

---
## 6.5 Check your User Settings <br>

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
| `bot.py`          | The main python bot logic              |
| `README.md`       | This guide                             |
| `LICENSE`         | Open-source MIT License                |

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to do anything with it.

---

## Questions?

If you're stuck or have questions, feel free to email me at [gkvyas3@gmail.com](mailto:gkvyas3@gmail.com). <br>
[https://www.gauravvyas.com](https://www.gauravvyas.com)


