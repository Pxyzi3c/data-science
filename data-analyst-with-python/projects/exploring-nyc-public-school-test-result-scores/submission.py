# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

def start():
    # Preview the data
    schools.head()
    
    # Clean data
    clean_data(schools)
    new_columns(schools)

    # Analyze data
    best_math_schools, top_10_schools, largest_std_dev = data_analysis(schools)

    return best_math_schools, top_10_schools, largest_std_dev

def clean_data(schools):
    integer_columns = ["percent_tested", "average_math", "average_reading", "average_writing"]
    schools[integer_columns] = schools[integer_columns].fillna(0)

    return schools

def new_columns(schools):
    schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
    schools_per_borough = schools.groupby("borough").size().dropna()
    schools["num_schools"] = schools["borough"].map(schools_per_borough)

    return schools

def data_analysis(schools):
    best_math_schools = schools[schools["average_math"] / 800 * 100 >= 80].sort_values("average_math", ascending=False)[["school_name", "average_math"]]
    top_10_schools = schools.sort_values("total_SAT", ascending=False).head(10)[["school_name", "total_SAT"]]
    # Group by borough and calculate total_SAT stats
    schools_by_borough = schools.groupby("borough").agg(
        num_schools=("borough", "count"),
        average_SAT=("total_SAT", "mean"),
        std_SAT=("total_SAT", "std"),
    )

    # Sort by std_SAT (descending) and get the first row (largest std)
    largest_std_dev = schools_by_borough.sort_values(by="std_SAT", ascending=False).head(1).round(2)

    return best_math_schools, top_10_schools, largest_std_dev

best_math_schools, top_10_schools, largest_std_dev = start()