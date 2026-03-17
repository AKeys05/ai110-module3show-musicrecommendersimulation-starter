from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores one song against user preferences using weighted matching.

    Returns:
        (total_score, reasons)
    """
    weights = {
        "mood": 25.0,
        "genre": 15.0,
        "energy": 15.0,
        "tempo_bpm": 10.0,
        "valence": 12.0,
        "danceability": 13.0,
        "acousticness": 10.0,
    }

    score = 0.0
    reasons: List[str] = []

    # Exact categorical matches
    pref_mood = user_prefs.get("mood")
    if pref_mood is not None and str(song.get("mood", "")).lower() == str(pref_mood).lower():
        mood_points = weights["mood"]
        score += mood_points
        reasons.append(f"mood match (+{mood_points:.1f})")

    pref_genre = user_prefs.get("genre")
    if pref_genre is not None and str(song.get("genre", "")).lower() == str(pref_genre).lower():
        genre_points = weights["genre"]
        score += genre_points
        reasons.append(f"genre match (+{genre_points:.1f})")

    # Numeric similarity features on [0, 1]
    for feature in ["energy", "valence", "danceability", "acousticness"]:
        if user_prefs.get(feature) is None or song.get(feature) is None:
            continue

        user_value = float(user_prefs[feature])
        song_value = float(song[feature])
        similarity = max(0.0, 1.0 - abs(song_value - user_value))
        points = weights[feature] * similarity

        score += points
        reasons.append(f"{feature} similarity {similarity:.2f} (+{points:.1f})")

    # Tempo similarity is normalized by 80 BPM window
    if user_prefs.get("tempo_bpm") is not None and song.get("tempo_bpm") is not None:
        tempo_diff = abs(float(song["tempo_bpm"]) - float(user_prefs["tempo_bpm"]))
        tempo_similarity = max(0.0, 1.0 - min(tempo_diff / 80.0, 1.0))
        tempo_points = weights["tempo_bpm"] * tempo_similarity

        score += tempo_points
        reasons.append(f"tempo similarity {tempo_similarity:.2f} (+{tempo_points:.1f})")

    if not reasons:
        reasons.append("no direct preference matches; baseline score 0.0")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
