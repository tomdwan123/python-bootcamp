# string_variable[start:end]

movie = "The Godfather"

print(movie[0:2]) # Th
print(movie[2:5]) # e G
print(movie[:2]) # Th
print(movie[4:]) # Godfather
print(movie[-2:]) # er

# string_variable[start:end:step]
print(movie[0:10:2]) # TeGda

print(movie[::]) # The Godfather
print(movie[::-1]) # rehtafdoG ehT