# Blackjack Game

A 1v1 Blackjack game built with Python and Pygame. The player competes against a computer dealer, with match history tracked via SQLite and visualized as a bar chart.

---

## Project Structure

```
blackjack/
├── card_image/              # Card face images (.png)
├── image/                   # UI images and button assets
├── music/                   # Background music
├── button.py                # Button component (click detection, rendering)
├── card.py                  # Deck generation and shuffling
├── db_conn.py               # SQLite database initialization
├── draw_chart.py            # Match history bar chart (matplotlib)
├── drawing_card.py          # Card rendering and game logic
├── game_note.py             # Match result persistence (SQLite + CSV export)
├── image_and_logo.py        # Image/asset loader
├── main_file_game.py        # Main game loop and state management
├── match_history.csv        # Exported match history
├── match_history.sql        # SQL schema
├── news.db                  # SQLite database
└── text_and_color.py        # Font and color definitions
```

---

## Prerequisites

- Python 3.8+
- pip

---

## Installation

```bash
git clone https://github.com/truonghoangthong/black_jack_game
cd black_jack_game
pip install pygame matplotlib pandas
```

---

## Running the Game

```bash
python main_file_game.py
```

On first run, the database will be initialized automatically from `match_history.sql`.

---

## How to Play

| Action | Control |
|--------|---------|
| Start game | Press `Space` on the intro screen |
| Draw a card | Click **Deal** (max 3 draws per round) |
| End your turn | Click **Stand** |
| New round | Click **New** after the result is shown |
| View history | Click **History** from the main menu |
| Go back | Click **Back** |

**Goal:** Get as close to 21 as possible without going over. Whoever is closest wins. The dealer plays automatically after you stand.

**Card values:**
- Number cards (2–10): face value
- Jack, Queen, King: 10
- Ace: 11 (or 1 if you have 4+ cards)
- 5-card hand under 21: automatic win

---

## Features

- Dealer AI with randomized draw logic based on score thresholds
- Match result tracking (wins, losses, ties) stored in SQLite
- CSV export of full match history on exit
- Bar chart visualization of cumulative results via matplotlib
- Background music and animated UI via Pygame

---

## Tech Stack

| Layer        | Technology          |
|--------------|---------------------|
| Game engine  | Pygame              |
| Database     | SQLite3             |
| Data export  | CSV (built-in)      |
| Visualization| matplotlib, pandas  |
| Language     | Python              |
