# SimpleMMO Bot 🤖

A Python-based automation bot for SimpleMMO that helps automate various in-game activities including traveling, gathering resources, and combat.

## 🎯 Features

- **Automated Travel**: Automatically takes steps to explore the game world
- **Resource Gathering**: Automatically performs various gathering activities:
  - Mining
  - Wood chopping
  - Fishing/Catching
  - Salvaging
  - Grabbing event loot
- **Combat Automation**: Automatically attacks NPCs and mobs
- **CAPTCHA Solving**: Uses Google's Gemini AI to solve CAPTCHAs automatically
- **Session Management**: Saves login sessions for convenience
- **Pause/Resume**: Ability to pause and resume the bot at any time
- **Real-time Statistics**: Displays live counters for all activities
- **User-friendly GUI**: Simple interface built with CustomTkinter

## 📋 Prerequisites

- Python 3.11.9 
- Windows 10/11 (tested on Windows)
- Active SimpleMMO account
- Google Gemini API key

## 🛠️ Dependencies

The bot requires the following Python packages:

```
google-generativeai
camoufox
pyautogui
Pillow
customtkinter
tkinterDnD
```

## ⚙️ Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/Basit2121/SimpleMMOBot.git
   cd SimpleMMOBot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install additional required packages**
   ```bash
   pip install -r requirements.txt
   camoufox install firefox
   ```

4. **Set up Google Gemini API**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Replace `'ENTER YOUR API KEY HERE'` in `app.py` line 85 with your actual API key

## 🚀 Setup & Usage

### First Time Setup

1. **Run the bot**
   ```bash
   python app.py
   ```

2. **Login to SimpleMMO**
   - Click the "Login" button in the GUI
   - A browser window will open to SimpleMMO login page
   - Log in with your credentials
   - The bot will automatically save your session

3. **Configure bot settings**
   - **Attack Mobs/NPCs**: Enable to automatically attack enemies
   - **Gather Loot**: Enable to automatically gather resources (mining, chopping, fishing, salvaging)
   - **Grab Event Loot**: Enable to automatically grab event items

4. **Start the bot**
   - Click the "Start" button to begin automation
   - Use "Pause" button to temporarily stop the bot
   - Use "Resume" button to continue

### Important Notes

- **Healing**: If you die in combat, the bot will pause and alert you. Heal your character and restart the bot.
- **CAPTCHA**: The bot automatically solves CAPTCHAs using AI, but may occasionally fail.
- **Speed**: Disabling gathering and attack features will make traveling much faster.
- **Session**: Your login session is saved in `session.json` - don't delete this file unless you need to re-login.

## 🎮 Game Activities

### Travel
- Automatically takes steps to explore the game world
- Handles CAPTCHA challenges automatically

### Resource Gathering
- **Mining**: Automatically mines when ore is available
- **Wood Chopping**: Cuts down trees when available
- **Fishing/Catching**: Catches fish and other creatures
- **Salvaging**: Salvages items from the environment
- **Event Loot**: Grabs special event items

### Combat
- Automatically attacks NPCs and mobs when encountered
- Handles combat sequences and retreats when necessary
- Alerts user if character dies

## 🔧 Configuration

### API Key Setup
In `app.py`, line 85, replace the placeholder with your Google Gemini API key:
```python
genai.configure(api_key='YOUR_ACTUAL_API_KEY_HERE')
```

### Customization
You can modify various settings in the code:
- **Delays**: Adjust timing between actions in the `perform_action()` function
- **Screen resolution**: Modify the `Screen()` constraints for different monitor setups
- **Activity preferences**: Enable/disable specific activities through the GUI

## 📊 Statistics

The bot displays real-time counters for:
- Steps taken
- Mining activities
- Combat encounters
- Salvaging operations
- Wood chopping
- Fishing/catching
- CAPTCHAs solved
- Event loot grabbed

## ⚠️ Disclaimer

- This bot is for educational purposes only
- Use at your own risk
- Respect the game's terms of service
- The developers are not responsible for any account actions taken by game administrators

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`

2. **API Key Issues**
   - Verify your Google Gemini API key is correct and has sufficient credits

3. **Session Expired**
   - Delete `session.json` and re-login through the bot

4. **CAPTCHA Failures**
   - The AI may occasionally fail to solve CAPTCHAs - this is normal
   - The bot will continue after a brief delay

5. **Browser Issues**
   - Ensure you have a stable internet connection
   - Try restarting the bot if browser automation fails

## 📝 License

This project is open source. Feel free to modify and distribute according to your needs.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For support, please open an issue on the GitHub repository or contact the developer.

---

**GitHub**: https://github.com/Basit2121/SimpleMMOBot