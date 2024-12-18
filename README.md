# Virtual Assistant (Nova)

## Overview
Nova is a Python-based virtual assistant project developed during the transition in May 2023. This assistant can perform a variety of tasks, including interacting with users through voice commands, fetching information from the internet, managing basic system operations, and more.

## Features
- **Greeting**: Welcomes the user based on the time of day.
- **Voice Commands**: Responds to user commands via speech recognition.
- **Time and Date**: Provides the current time and date.
- **YouTube Playback**: Plays requested videos on YouTube.
- **Web Search**: Searches for information on Google and YouTube.
- **Wikipedia Integration**: Fetches summaries from Wikipedia.
- **Web Browsing**: Opens websites and specific tools like WhatsApp Web.
- **Location Search**: Locates places on Google Maps.
- **Weather Updates**: Retrieves the current temperature for a specified city.
- **Notes Management**: Allows users to take and review notes.
- **Screenshot Capture**: Takes a screenshot of the current screen.
- **Volume Control**: Adjusts the system volume.
- **Custom Interactions**: Engages in playful activities like mimicking a Talking Tom-style conversation.
- **Sleep and Shutdown**: Can temporarily sleep or shut down based on commands.

## Prerequisites
To use this project, the following dependencies need to be installed:

- Python 3.7 or higher
- Required Python libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `pywhatkit`
  - `datetime` (standard library)
  - `wikipedia`
  - `webbrowser` (standard library)
  - `requests`
  - `bs4`
  - `pyautogui`

Install dependencies using:
```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia requests beautifulsoup4 pyautogui
```

## How to Use
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the Python script:
   ```bash
   python main.py
   ```

3. Activate Nova: Say "Wake up" to initialize Nova, and start interacting using voice commands.

## Voice Commands
Here is a list of sample commands Nova can handle:

### General Commands
- "What time is it?"
- "What is the date today?"

### Entertainment
- "Play [song name]"

### Search
- "Search [query]"
- "Search [query] on YouTube"
- "Tell me about [topic] from Wikipedia"

### Utilities
- "Open [website name]"
- "Locate [place]"
- "What is the temperature in [city]?"

### System Controls
- "Take a note"
- "Show note"
- "Take a screenshot"
- "Increase volume"
- "Mute"

### Playful Interaction
- "Talking Tom"

### Shutdown
- "Sleep"
- "Turn off"
  
## Future Improvements
- Enhance error handling for smoother user experience.
- Add support for additional languages.
- Integrate AI-powered natural language processing for better command understanding.
- Expand capabilities to include email handling and advanced system controls.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
[Jovin Paul J]
- Email: [jovinpaulj@gmail.com]
- GitHub: [https://github.com/JovinPaul-J]

## Acknowledgments
Special thanks to the open-source community,Python and all the libraries used in this project,GeeksforGeeks, and YouTube for their invaluable resources.

