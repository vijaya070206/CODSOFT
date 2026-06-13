# Task 4 — Movie Recommendation System

**CodSoft AI Internship**

## Overview
A movie recommendation system built in pure Python using two filtering techniques — **Content-Based Filtering** and **Collaborative Filtering** — with no external libraries required.

## Features
- Content-Based Filtering using Jaccard similarity (matches movies by genre)
- Collaborative Filtering using Cosine similarity (matches users by taste)
- Dataset of 20 movies including Hollywood and Indian films
- 6 pre-built user profiles for collaborative filtering
- Interactive menu-driven interface

## How to Run

```bash
python recommendation.py
```

No pip installs needed — uses only Python's built-in `math` library.

## Sample Output

```
  Choose an option:
  1. Content-Based Recommendations (by genre)
  2. Collaborative Filtering (by similar users)
  3. Show all movies
  4. Exit

  Enter a movie ID you like: 1

  Because you liked 'Inception':
  1. The Matrix        | Sci-Fi, Action, Thriller
  2. The Dark Knight   | Action, Thriller, Crime
  3. Interstellar      | Sci-Fi, Drama, Adventure
```

## Tech Used
- Python 3.x
- Jaccard Similarity (Content-Based)
- Cosine Similarity (Collaborative Filtering)
- No external libraries

## Author
Bandi Vijaya Siva Sai Naga Jyothi  
CodSoft AI Internship — Task 4
