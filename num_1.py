# START
movie_length: int = int(input("Enter the length of the movie: "))
hours: int = movie_length // 60
minutes: int = movie_length % 60
print(f"length of the movie is: {hours} hours and {minutes} minutes")
# END
