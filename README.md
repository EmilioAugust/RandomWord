# 🧠 Random English Words API

A simple yet powerful **FastAPI** application that serves random English words — perfect for learners!  
You can also select your **English proficiency level (A1–C1)** to get words tailored to your vocabulary.

---

## 🚀 Features

- 🎲 **Get random English words with definitions** via API  
- 🧩 **Filter by difficulty level** (A1, A2, B1, B2, C1)
- ⚡ Built with **FastAPI** — modern, fast, and async  
- 🌍 Perfect for integrating into learning apps, chatbots, or word games  

---

## 🛠️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [Supabase](https://supabase.com/)
- **Language:** Python 3.10+
- **Deployment:** [Vercel](https://vercel.com/)
- **Data Source:** 8,000+ English words with CEFR levels

---

## 📦 Installation

```bash
git clone https://github.com/EmilioAugust/RandomWord.git
cd RandomWord
pip install -r requirements.txt
```

---

## ▶️ Running the App
```bash
uvicorn main:app --reload
```
Then open your browser at:
👉 http://127.0.0.1:8000/docs

Or you can just open this website, if you don't want to do everything above:
👉 https://random-word-blond.vercel.app

---

## 📚 API Endpoints

| Method | Endpoint           | Description                                 |
| ------ | ------------------ | ------------------------------------------- |
| `GET`  | [`/v1/random`](https://random-word-blond.vercel.app/v1/random)          | Get a random English word                   |
| `GET`  | [`/v1/random/a1`](https://random-word-blond.vercel.app/v1/random/a1) | Get a random word filtered by level (A1–C1) |

---

## 🧩 Future Improvements
- ☐ Add pronunciation (audio files or transcription)
- ☐ Support multiple languages

---

## 🧾 License

This project is licensed under the MIT License — feel free to use and modify it.
