# File Handling in Python

# 1. Opening a file in write mode
file = open("student.txt", "w")

# 2. Writing data into the file
file.write("Name: Anjali\n")
file.write("Course: B.Tech CSE\n")
file.write("Year: Second Year\n")

# 3. Closing the file
file.close()

print("Data written successfully.")


# 4. Opening the file in read mode
file = open("student.txt", "r")

# 5. Reading the complete file
data = file.read()

print("\nFile Content:")
print(data)

# 6. Closing the file
file.close()


# 7. Opening the file in append mode
file = open("student.txt", "a")

# 8. Appending new data
file.write("Subject: Advanced Python\n")

# 9. Closing the file
file.close()

print("Data appended successfully.")


# 10. Opening the file again in read mode
file = open("student.txt", "r")

print("\nUpdated File Content:")
print(file.read())

# 11. Closing the file
file.close()
