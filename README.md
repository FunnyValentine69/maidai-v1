<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=2,3,12&height=200&section=header&text=☕%20Maid%20Cafe%20Dating%20Sim&fontSize=42&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=「いらっしゃいませ、ご主人様～！」&descSize=18&descAlignY=58" width="100%" />
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-meet-your-maids">Characters</a> •
  <a href="#-how-to-play">How to Play</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python_3-E63946?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MIT_License-1a1a2e?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama_+_llama3.2-C2185B?style=for-the-badge&logo=ollama&logoColor=white" />
  <img src="https://img.shields.io/badge/Terminal_Game-FF6B6B?style=for-the-badge&logo=windowsterminal&logoColor=white" />
</p>

<br>

<p align="center">
  <i>A charming terminal dating sim set in an anime maid cafe.<br>Chat with three adorable maids, build relationships, and unlock romantic endings!</i>
</p>

<br>

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 💕 Three Romance Routes
Each maid has her own personality, story arc, and **3 unique endings** — romantic, friendship, and passionate.

</td>
<td width="50%" valign="top">

### 📈 Affection System
Build relationships through conversation. Compliments, kindness, and orders raise affection toward confession scenes.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🤖 AI-Powered Dialogue
Dynamic responses via **Ollama + llama3.2**. Hardcoded reactions for speed, AI fallback for variety.

</td>
<td width="50%" valign="top">

### 🍰 Cafe Menu
Order from 7 menu items — each maid reacts uniquely to your orders with in-character dialogue.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💌 Confession Scenes
At 60+ affection, a fully written after-hours confession scene plays out with branching choices.

</td>
<td width="50%" valign="top">

### 🎭 Distinct Personalities
From shy whispers to playful teasing — each maid stays in character with unique speech patterns and mannerisms.

</td>
</tr>
</table>

---

## 🚀 Quick Start

> [!IMPORTANT]
> Requires [Ollama](https://ollama.ai/) running locally with the `llama3.2` model.

```bash
# Clone the repo
git clone https://github.com/FunnyValentine69/maidai-v1.git
cd maidai-v1

# Install dependencies
pip install ollama

# Pull the AI model
ollama pull llama3.2

# Start the game
python maid_cafe.py
```

---

## 💖 Meet Your Maids

<table>
<tr>
<td align="center" width="33%">

### 🌸 Sakura
**Enthusiastic & Sweet**

*"Irasshaimase, Master~! I'll do my very best to serve you! Ganbarimasu~!"*

Energetic, warm, uses lots of exclamation marks. Always eager to brighten your day.

</td>
<td align="center" width="33%">

### 🦋 Yuki
**Shy & Soft-spoken**

*"W-Welcome, Master... I'm so glad you came..."*

Gentle, nervous, speaks in whispers with ellipses. Slowly opens up as you get closer.

</td>
<td align="center" width="33%">

### 🔥 Akira
**Playful & Teasing**

*"Well well well~ Look who decided to grace us with their presence! Ufufu~"*

Confident, flirty, keeps you on your toes with witty banter and bold remarks.

</td>
</tr>
</table>

---

## 💗 Affection System

Build your bond through conversations, compliments, and kindness:

| Progress | Points | Status | Hearts |
|:--------:|:------:|:------:|:------:|
| 🌱 | 10+ | Warming Up | ❤️🤍🤍🤍🤍 |
| 🌸 | 25+ | Close Friends | ❤️❤️🤍🤍🤍 |
| 💗 | 50+ | Deep Bond | ❤️❤️❤️❤️🤍 |
| 💝 | 60+ | Confession! | ❤️❤️❤️❤️❤️ |

<details>
<summary><b>How affection works</b></summary>

<br>

- **Compliments** → `+3 pts` (use words like *cute, pretty, amazing, lovely*)
- **Politeness** → `+1 pt` (saying *thank you, arigatou*)
- **Caring** → `+1 pt` (asking *how are you*)
- **Rude words** → `-5 pts` (insults drop affection fast)
- **Threshold unlocks** trigger special dialogue from your maid
- At **60+ points**, the after-hours confession scene begins

</details>

---

## 🎮 How to Play

1. **Choose your maid** — pick from Sakura, Yuki, or Akira
2. **Chat freely** — type anything to talk with your maid
3. **Order food** — type `menu` to see offerings, then type an item name
4. **Build affection** — compliment her, be polite, ask how she's doing
5. **Unlock the confession** — reach 60+ affection for a special scene
6. **Choose your ending** — romantic, friendship, or passionate

> [!TIP]
> Each maid has completely different confession scenes and epilogues. Replay to see all 9 endings!

<details>
<summary><b>🍰 Menu Items</b></summary>

<br>

| Item | Price |
|:-----|------:|
| Coffee | ¥450 |
| Tea | ¥400 |
| Cake | ¥550 |
| Omurice | ¥750 |
| Parfait | ¥650 |
| Cookies | ¥350 |
| Milkshake | ¥500 |

</details>

---

## 🗺️ Roadmap

<details>
<summary><b>Planned features</b></summary>

<br>

- [ ] **ZZZ-style character artwork** — visual portraits inspired by Zenless Zone Zero
- [ ] **Visual novel UI** — full graphical interface upgrade
- [ ] **Additional maids** — expand the cafe staff
- [ ] **Voice lines** — character audio
- [ ] **Save system** — persistent affection across sessions

</details>

---

## 🛠️ Tech Stack

| Technology | Purpose |
|:-----------|:--------|
| **Python 3** | Core game engine |
| **Ollama** | Local AI inference |
| **llama3.2** | Language model for dynamic maid responses |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<table>
<tr>
<td align="center">

**Created by [FunnyValentine69](https://github.com/FunnyValentine69)**

</td>
</tr>
</table>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=2,3,12&height=80&section=footer&animation=twinkling" width="100%" />
</p>
