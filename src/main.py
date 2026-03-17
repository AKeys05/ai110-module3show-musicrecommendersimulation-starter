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
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "tempo_bpm": 150.0,
        "valence": 0.45,
        "danceability": 0.58,
        "acousticness": 0.10,
    },
    "tie": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.39,
        "tempo_bpm": 75.0,
        "valence": 0.58,
        "danceability": 0.60,
        "acousticness": 0.79,
    },
    "conflicting": {
        "genre": "rock",
        "mood": "chill",
        "energy": 0.92,
        "tempo_bpm": 150.0,
        "valence": 0.65,
        "danceability": 0.40,
        "acousticness": 0.85,
    },
    "single_feature": {
        "mood": "chill",
        "energy": 0.50,
        "tempo_bpm": 120.0,
        "valence": 0.50,
        "danceability": 0.50,
        "acousticness": 0.50,
    },
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
