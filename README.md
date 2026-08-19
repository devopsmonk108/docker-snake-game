# 🐍 Dockerized Snake Game

A classic Snake game built with **Flask** and **JavaScript**, fully containerized with **Docker**. Playable directly in the browser, with a live speed control slider.

---

## 🎮 Features

- Classic Snake gameplay — arrow keys to move
- Live score tracking
- **Adjustable speed slider** — change game speed on the fly, even mid-game
- Game over screen with instant restart (press `Space`)
- Fully containerized — runs identically on any machine with Docker installed

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| Frontend | HTML5 Canvas + JavaScript |
| Containerization | Docker |

---

## 🏗️ Architecture

Flask serves a single HTML page containing embedded JavaScript. Once the page loads in the browser, **all game logic runs client-side** — movement, collision detection, scoring, and speed control are handled entirely by JavaScript in the browser's engine. Docker's only job is to package and serve the app consistently across environments.

```
Browser (JavaScript game loop) <- HTTP <- Flask (Python) <- Docker container
```

---

## 🚀 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/) installed and running

### Build the image
```bash
docker build -t snake-game .
```

### Run the container
```bash
docker run -d --name snake -p 5000:5000 snake-game
```

### Play
Open your browser to:
```
http://localhost:5000
```

---

## 🎯 Controls

| Key | Action |
|---|---|
| Arrow keys | Move the snake |
| `Space` | Restart after game over |
| Speed slider | Adjust game speed live (40ms - 300ms per frame) |

---

## 📂 Project Structure

```
.
├── app.py             # Flask server + embedded game (HTML/CSS/JS)
├── requirements.txt   # Python dependencies
├── Dockerfile          # Container build instructions
└── .gitignore
```

---

## 📄 License

This project is open source and available for anyone to use or build upon.
