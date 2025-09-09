# Jarvis-Voice-Assistant 🗣️🤖

A simple Python-based voice assistant that can recognize speech, respond with text-to-speech, open websites, play music, and even fetch the latest news headlines using the News API.  

---

## ✨ Features
- 🎙️ Speech recognition with wake word **"Jarvis"**
- 🗣️ Text-to-speech responses using `pyttsx3`
- 🌐 Open popular websites like Google, YouTube, Facebook, Instagram
- 🎶 Play music from a custom `musicLibrary`
- 📰 Get real-time top headlines using **News API**
- 🔄 Continuous listening loop for commands

---

## 🛠️ Tech Stack
- **Python 3**
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)  
- [pyttsx3](https://pypi.org/project/pyttsx3/)  
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)  
- [requests](https://pypi.org/project/requests/)  
- Custom `musicLibrary.py`

---

## 📂 Project Structure
    Jarvis-Voice-Assistant    
      │--main.py
      │-- musicLibrary.py
      │-- README.md


---

## ⚙️ Setup & Installation
1. Clone the repository:
    ```
    git clone https://github.com/Tarun-Gautam-915/Jarvis-Voice-Assistant.git
    cd Jarvis-Voice-Assistant
2. Install dependencies:
    ```
    pip install speechrecognition pyttsx3 requests
  
3. Create a file musicLibrary.py and add your music links in dictionary format:
    ```
    music = {
        "songname": "https://youtube.com/link-to-song"
    }
4. Replace the placeholder News API key in main.py with your own key from NewsAPI.

## ▶️ Usage
  1. Run the assistant:
        ```
        python main.py
2. Say "Jarvis" to activate, then give commands like:
    ```
    "open google"
    "open youtube"
    "play songname"
    "news"
## 📌 Example Interaction
  
    User: Jarvis
    Jarvis: Ya
    User: open google
    Jarvis: Opening Google...
    
## 🚧 Future Enhancements
- Add weather updates 🌦️
- Add reminder/notes functionality 📝
- Integrate with smart home devices 💡
- Support multiple wake words

## 📜 License
This project is open-source and available under the MIT License.

## ✨ Author
Created by Tarun 🎉
