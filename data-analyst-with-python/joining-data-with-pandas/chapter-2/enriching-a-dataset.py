'''
Setting how='left' with the .merge()method is a useful technique for enriching or enhancing a dataset with additional information from a different table. In this exercise, you will start off with a sample of movie data from the movie series Toy Story. Your goal is to enrich this data by adding the marketing tag line for each movie. You will compare the results of a left join versus an inner join.

The toy_story DataFrame contains the Toy Story movies. The toy_story and taglines DataFrames have been loaded for you.
'''

# 1 - Merge toy_story and taglines on the id column with a left join, and save the result as toystory_tag.
# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on="id", how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# 2 - With toy_story as the left table, merge to it taglines on the id column with an inner join, and save as toystory_tag.
# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on="id")
toystory_tag_left = toy_story.merge(taglines, on="id", how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
