def main():
    courses = {}
    while True:
        course_id = input("Enter course ID (or type 'exit' to finish): ")
        if course_id.lower() == 'exit':
            break
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    subject = input("Enter the subject code to search for (e.g., 'COS'): ")
    print(f"\nCourses for subject '{subject}':")
    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True
    if not found:
        print("No courses found for that subject.")
if __name__ == "__main__":
    main()

# Matthew Beekman
# 10/24/2024
# Program 5