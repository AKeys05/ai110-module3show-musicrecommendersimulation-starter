"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    # Allows running as a script: python src/main.py
    from recommender import load_songs, recommend_songs

# Change this one value to switch the default profile used by main().
ACTIVE_PROFILE = "default"

PROFILE_PRESETS = {
    "default": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.60,
        "tempo_bpm": 110.0,
        "valence": 0.65,
        "danceability": 0.65,
        "acousticness": 0.40
    },
    "acoustic_focus": {
        "genre": "folk",
        "mood": "nostalgic",
        "energy": 0.38,
        "tempo_bpm": 88.0,
        "valence": 0.66,
        "danceability": 0.45,
        "acousticness": 0.92
    },
    "club_rush": {
        "genre": "edm",
        "mood": "energetic",
        "energy": 0.97,
        "tempo_bpm": 130.0,
        "valence": 0.72,
        "danceability": 0.93,
        "acousticness": 0.03
    },
    "punk_spirit": {
        "genre": "punk",
        "mood": "rebellious",
        "energy": 0.95,
        "tempo_bpm": 176.0,
        "valence": 0.42,
        "danceability": 0.56,
        "acousticness": 0.05,
    }
}

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded {len(songs)} songs.")

    if ACTIVE_PROFILE not in PROFILE_PRESETS:
        available = ", ".join(sorted(PROFILE_PRESETS.keys()))
        raise ValueError(f"Unknown ACTIVE_PROFILE '{ACTIVE_PROFILE}'. Choose one of: {available}")

    user_prefs = PROFILE_PRESETS[ACTIVE_PROFILE]
    print(f"Using profile: {ACTIVE_PROFILE}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 60)
    print("Top Recommendations")
    print("=" * 60)

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print(f"\n{idx}. {song['title']}")
        print(f"   Final Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
