import this
print(this)
numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
result = [number for number in numbers if number % 2 == 0]
print(result)
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thankyou very much."
count_spaces = len([char for char in story if char == ' '])
print(count_spaces)
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thankyou very much."
count_words = len([word for word in story.split() if len(word) > 4])
print(count_words)
