# Rythm Music Player 🎵

A simple yet elegant music player built with Python, using Tkinter for the GUI and Pygame for audio playback. This project serves as a practical example of desktop application development with Python.

After many years, I've revisited this project to fix a long-standing issue that prevented the application icon from displaying correctly on Linux systems. This guide provides the updated and corrected way to set up and run the application.

## Features

* **Themed & Modern UI**: Built with Tkinter and styled using the `arc` theme from the `ttkthemes` library for a clean look.
* **Core Playback Controls**: Full control with **Play**, **Pause**, **Stop**, and **Rewind** functionality.
* **Dynamic Playlist**: Easily **add** individual songs to the playlist and **remove** them as needed.
* **Real-time Audio Info**: Displays the currently playing song title, total duration, and a live-updating current timestamp.
* **Volume Control**: Features an interactive volume slider and a dedicated **Mute/Unmute** toggle button.
* **Cross-Platform Compatibility**: The original icon issue on Linux has been resolved by using `PhotoImage` and `iconphoto`, ensuring the app looks and feels native.
* **Menu Bar**: A simple menu for opening files, exiting the application, and viewing app info.

---

## Technology Stack

* **Python 3**: The core programming language.
* **Tkinter**: Python's standard library for creating graphical user interfaces (GUIs).
* **Pygame (mixer module)**: Used for its robust and straightforward audio-playing capabilities.
* **ttkthemes**: Provides modern styling for Tkinter's themed widgets (ttk).
* **mutagen**: A powerful library for handling audio metadata, used here to read the length of MP3 files.

---

## Installation and Setup (Linux)
Information for installing the packages required to run this in Installation.pdf.
