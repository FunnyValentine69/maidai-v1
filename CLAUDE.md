# Maid Cafe Dating Sim

A terminal-based anime maid cafe dating simulator featuring three unique maid characters with distinct personalities, an affection system, and dynamic AI-powered conversations.

## Project Overview

This is an interactive dating sim set in a cozy maid cafe where players can chat with, order from, and romance three adorable maids. Each maid has her own personality, dialogue, and romance route with multiple endings.

## Characters

### Sakura
- **Personality:** Enthusiastic and sweet
- **Traits:** Energetic, warm, always eager to make customers happy
- **Style:** Uses lots of exclamation marks, cheerful expressions, and calls you "Master~!"

### Yuki
- **Personality:** Shy and soft-spoken
- **Traits:** Gentle, nervous around new people, secretly caring
- **Style:** Speaks quietly, uses ellipses, blushes frequently, gradually opens up

### Akira
- **Personality:** Playful and teasing
- **Traits:** Confident, flirty, loves to tease customers
- **Style:** Witty remarks, playful winks, keeps you on your toes

## Key Features

### Affection System
- Each maid tracks individual affection points per session
- **Thresholds:**
  - 10 points - Maid starts warming up to you
  - 25 points - Friendship level unlocked
  - 50 points - Deep bond established
  - 60 points - Confession scene available

### Romance & Endings
- Confession scenes trigger at 60+ affection points
- **3 unique endings per character** based on your choices
- Each ending reflects your relationship journey with that maid

### Menu System
- **7 menu items** available to order
- Ordering food is a way to interact and build affection
- Each maid has unique reactions to different orders

### AI Integration
- Powered by **Ollama** with the **llama3.2** model
- Hardcoded responses for common interactions (speed optimization)
- AI fallback for dynamic, contextual conversations
- Maids stay in character with personality-appropriate responses

## Technical Details

- **Language:** Python 3
- **AI Backend:** Ollama (local LLM)
- **Model:** llama3.2
- **Response Strategy:** Hardcoded responses for speed, AI fallback for flexibility
- **Data Persistence:** None (session-based, resets on restart)
- **Dependencies:** See `requirements.txt`

## Current Status

**Fully Functional** - Complete dating sim experience with:
- All three maids fully implemented
- Complete romance routes for each character
- All confession scenes and endings written
- Working affection system
- Menu ordering system
- AI-powered dynamic conversations

## Future Plans

- **ZZZ-style character artwork** - Add visual character portraits inspired by Zenless Zone Zero's art style
- **Visual novel UI** - Potential upgrade to a full visual novel interface
- **Additional maids** - Expand the cafe staff
- **Voice lines** - Character audio
- **Save system** - Persistent affection across sessions

---

*Welcome to the Maid Cafe, Master~!*
