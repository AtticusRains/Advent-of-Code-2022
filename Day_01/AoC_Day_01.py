file = open("input_day_01")
lines = file.readlines()

most_calories = 0
second_most = 0
third_most = 0
current_calories = 0
for line in lines:
    if line != '\n':
        current_calories += int(line)
    elif current_calories > most_calories:
        third_most = second_most
        second_most = most_calories
        most_calories = current_calories
        current_calories = 0
    elif current_calories > second_most:
        third_most = second_most
        second_most = current_calories
        current_calories = 0
    elif current_calories > third_most:
        third_most = current_calories
        current_calories = 0
    else:
        current_calories = 0

print("Most calories: ")
print(most_calories)
print("Second most calories: ")
print(second_most)
print("third most calories: ")
print(third_most)
print("total:")
print(most_calories + second_most + third_most)