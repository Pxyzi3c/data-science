# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

def start():
    # filtering
    movies_df = get_show_type("Movie")
    tv_shows_df = get_show_type("TV Show")
    
    # calculating statistics
    movies_df["duration_category"] = movies_df["duration"].apply(categorize_by_duration)
    movies_90s_df, duration, short_movie_count = analyze_90s_movies(movies_df)
    
    data_visualization(movies_90s_df["release_year"], movies_90s_df["duration"])
    
    return duration, short_movie_count, movies_90s_df
    
def analyze_90s_movies(netflix_df):
    movies_90s_df = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] < 2000)]
    duration = movies_90s_df["duration"].value_counts().idxmax()
    short_action_movies = movies_90s_df[(movies_90s_df["genre"] == "Action") & (movies_90s_df["duration_category"] == "Short")]
    short_movie_count = len(short_action_movies) 
    
    return movies_90s_df, duration, short_movie_count

def data_visualization(release_date, duration):
    plt.figure(figsize=(12, 6)) # Set the figure size
    
    plt.subplot(1, 2, 1)
    scatter_plot(release_date, duration)
    plt.subplot(1, 2, 2)
    histogram(duration)
    
    plt.tight_layout()  # Adjust spacing between subplots
    plt.show()
    
def scatter_plot(data1, data2):
    plt.scatter(data1, data2, color="blue", alpha=0.5)
    plt.xlabel("Release Year")
    plt.ylabel("Movie Duration by Release Year (minutes)")
    plt.title("Movie Duration by Release Year (1990s)")
    plt.grid(True)
    
def histogram(data):
    plt.hist(data, bins=10, edgecolor='black')
    plt.xlabel("Movie Duration (minutes)")
    plt.ylabel("Number of Movies")
    plt.title("Most Frequent Movie Duration")
    plt.grid(True)
    
def get_show_type(type):
    return netflix_df[netflix_df["type"] == type]

def categorize_by_duration(duration):
    if duration <= 90:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"

duration, short_movie_count, movies_90s_df = start()
