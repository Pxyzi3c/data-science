'''
The Movie Database is supported by volunteers going out into the world, collecting data, and entering it into the database. This includes financial data, such as movie budget and revenue. If you wanted to know which movies are still missing data, you could use a left join to identify them. Practice using a left join by merging the movies table and the financials table.

The movies and financials tables have been loaded for you.
'''

# 1 - Merge the movies table, as the left table, with the financials table using a left join, and save the result to movies_financials.
# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on="id", how="left")

print(movies_financials)

# 2 - Count the number of rows in movies_financials with a null value in the budget column.
# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)