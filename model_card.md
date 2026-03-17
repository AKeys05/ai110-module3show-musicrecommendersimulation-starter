# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MoodMatch**  

---

## 2. Intended Use  

This is a music recommender model particularly intended for classroom exploration. It generates short numerical-based explanations of each provided recommendation and does not include much of the nuance and specificity of modern music streaming systems. It assumes that each user will have values for most (if not all) of the following musical preferences: mood, genre, energy, tempo in bpm, valence, danceability, and acousticness. It provides 5 of the top songs from its internal dataset that the user is most likely to enjoy based off of their preferences.

---

## 3. How the Model Works  

First, a user creates a profile that lists their specific music preferences. Mood (worth 25 points) and genre (worth 15 points) are only given either full points or a zero, based upon whether its an exact match to the profile. Tempo (worth 10 points) uses a unique similarity formula whose value is multiplied by 10 to calculate its number of points. The remaining features (Energy(15), Valence(12), Danceability(13) and Acousticness(10)) also use a similarity formula whose value is multipled by the feature weight to calculate its point total. Each of the features individual totals are summed up to calculate the final score out of 100. A score is assigned to each song in the model's dataset and ranked to provide a list of recommendations to the user.

---

## 4. Data  

The model uses a dataset of 18 total songs: ten from the original file and 8 added songs. It consists of the following genres: pop, lofi, rock, ambient, jazz, EDM, k-pop, punk, country, indie, synthwave, afrobeat, latin, and folk. The moods represented are happy, chill, intense, moody, relaxed, melancholic, hopeful, energetic, playful, euphoric, nostalgic, and focused. While there may be some niche categories that are potentially not represented, it covers an acceptable range in terms of musical taste.

---

## 5. Strengths  

The system works well for clear, coherent preferences where the mood and genre align with the features (e.g., lofi + chill + low tempo + high acousticness). It handles partial profiles reasonably well by still being able to rank based off the available fields instead of failing. I also think the scoring algorithm is able to return very specific scoring details that makes it easier to assign a ranking than if they were too broad.

---

## 6. Limitations and Bias 


The most significant limitation or "filter-bubble" within the current scoring logic is that mood and genre are only scored based upon exact equality. This means one exact label can dominate the ranking and lock users into a narrow category. Also, the top-k ranking structure amplifies repetition and order bias. It doesn't take into account diversity, novelty or artist caps so the same profile will likely get the same list of recommendations each time.

---

## 7. Evaluation  

I tested four distinct user profiles on my music recommender system: default, acoustic focus, club rush and punk spirit. I was looking for verification that the five recommendations had accurately calculated song scores that matched the vibe of the profile in terms of the tempo, energy, mood, etc. I felt that all 4 of the tested profiles returned expected results (e.g., mellow study music for acoustic focus and high-energy dancing songs for club rush). I also ran a few tests with some critical edge cases such as if the profile has conflicting preferences, tied preferences, or a single feature that dominates the rest. In all cases, it again behaved as expected by heavily favoring the highest-weighted mood or genre matches, and then using the numeric similarities to break close calls.

---

## 8. Future Work  

A key feature that would improve the model is adding diversity controls in top-k to avoid it from recommending overly similar tracks. Similarly, explicit tie breaking rules based upon popularity, diversity or novelty would help make near-tie ranking more intentional and clear. Lastly, another core feature improvement would be altering explainability to be less numeric based and rather based on categorical/semantic meaning so as to be more easily understood by users.

---

## 9. Personal Reflection  

Just from making this simple music recommender system, I learned how much goes into the behind the scenes of the advanced tools we use on popular platforms today. In theory the process of assigning scores to each song and producing a ranked list based upon user preferences sounds intuitive, but creating one yourself truly makes you wonder how complex some of the modern systems' compatability scoring algorithms are. It encouraged me to appreciate the accuracy and reliability of the one I use day-to-day, especially considering how much larger their song database is.