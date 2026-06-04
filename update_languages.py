import json

language_map = {
    "Sita Ramam": ["Telugu", "Hindi", "Tamil", "Malayalam"],
    "RRR": ["Telugu", "Hindi", "Tamil", "Malayalam", "Kannada"],
    "Aditya 369": ["Telugu"],
    "Jersey": ["Telugu", "Hindi", "Tamil"],
    "Arjun Reddy": ["Telugu", "Hindi", "Tamil"],
    "Baahubali": ["Telugu", "Hindi", "Tamil", "Malayalam"],
    "Eega": ["Telugu", "Hindi", "Tamil", "Malayalam"],
    "Pushpa": ["Telugu", "Hindi", "Tamil", "Malayalam", "Kannada"],
    "Salaar": ["Telugu", "Hindi", "Tamil", "Malayalam", "Kannada"],
    "Mahanati": ["Telugu", "Tamil", "Malayalam"],

    "Dangal": ["Hindi", "Telugu", "Tamil"],
    "3 Idiots": ["Hindi", "Telugu", "Tamil"],
    "PK": ["Hindi", "Telugu", "Tamil"],
    "Taare Zameen Par": ["Hindi"],
    "Chak De India": ["Hindi"],
    "Zindagi Na Milegi Dobara": ["Hindi"],
    "Queen": ["Hindi"],
    "War": ["Hindi", "Telugu", "Tamil"],
    "Drishyam 2": ["Hindi", "Telugu", "Tamil"],
    "Shershaah": ["Hindi"],

    "Interstellar": ["English", "Hindi", "Telugu", "Tamil"],
    "Inception": ["English", "Hindi", "Telugu", "Tamil"],
    "The Martian": ["English", "Hindi", "Telugu", "Tamil"],
    "The Dark Knight": ["English", "Hindi", "Telugu", "Tamil"],
    "Avengers Endgame": ["English", "Hindi", "Telugu", "Tamil"],
    "Titanic": ["English", "Hindi", "Telugu", "Tamil"],
    "Forrest Gump": ["English", "Hindi"],
    "The Pursuit of Happyness": ["English", "Hindi"],
    "The Conjuring": ["English", "Hindi", "Tamil"],
    "Jumanji": ["English", "Hindi", "Telugu", "Tamil"],

    "Vikram": ["Tamil", "Telugu", "Hindi", "Malayalam"],
    "Master": ["Tamil", "Telugu", "Hindi"],
    "Leo": ["Tamil", "Telugu", "Hindi", "Kannada"],
    "96": ["Tamil", "Telugu"],
    "Super Deluxe": ["Tamil", "Telugu", "Malayalam"],
    "Kaithi": ["Tamil", "Telugu", "Hindi"],
    "Soorarai Pottru": ["Tamil", "Telugu", "Hindi"],
    "Ghajini": ["Tamil", "Telugu", "Hindi"],
    "Ratsasan": ["Tamil", "Telugu", "Hindi"],
    "Mersal": ["Tamil", "Telugu", "Hindi"],

    "Premam": ["Malayalam", "Telugu", "Tamil"],
    "Drishyam": ["Malayalam", "Telugu", "Tamil", "Hindi"],
    "Lucifer": ["Malayalam", "Telugu", "Tamil", "Hindi"],
    "Bangalore Days": ["Malayalam", "Telugu", "Tamil"],
    "Kumbalangi Nights": ["Malayalam", "Telugu", "Tamil"],
    "Uyare": ["Malayalam", "Telugu", "Tamil"],
    "Minnal Murali": ["Malayalam", "Telugu", "Tamil", "Hindi"],
    "Hridayam": ["Malayalam", "Telugu", "Tamil"],
    "2018": ["Malayalam", "Telugu", "Tamil", "Hindi"],
    "Thallumaala": ["Malayalam", "Telugu", "Tamil"],

    "KGF": ["Kannada", "Telugu", "Hindi", "Tamil", "Malayalam"],
    "Kantara": ["Kannada", "Telugu", "Hindi", "Tamil", "Malayalam"],
    "777 Charlie": ["Kannada", "Telugu", "Hindi", "Tamil", "Malayalam"],
    "Kirik Party": ["Kannada", "Telugu", "Hindi"],
    "U Turn": ["Kannada", "Telugu", "Tamil", "Hindi"],
    "Lucia": ["Kannada", "Telugu", "Hindi"],
    "Avane Srimannarayana": ["Kannada", "Telugu", "Hindi", "Tamil"],
    "Dia": ["Kannada", "Telugu", "Tamil"],
    "Roberrt": ["Kannada", "Telugu", "Hindi"],
    "James": ["Kannada", "Telugu", "Hindi"]
}

with open("backend/movies.json", "r", encoding="utf-8") as file:
    movies = json.load(file)

for movie in movies:
    movie_name = movie["name"]

    if movie_name in language_map:
        movie["availableLanguages"] = language_map[movie_name]
    else:
        movie["availableLanguages"] = [movie["language"]]

with open("backend/movies.json", "w", encoding="utf-8") as file:
    json.dump(movies, file, indent=2, ensure_ascii=False)

print("Available languages added successfully!")