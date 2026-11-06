"""Small in-memory data layer for the Nascomsoft training demo."""

COURSES = [
    {
        "course_id": 1,
        "title": "Python Programming",
        "duration": "4 Weeks",
        "description": "Programming foundations with Python.",
    },
    {
        "course_id": 2,
        "title": "Software Development with Python",
        "duration": "4 Weeks",
        "description": "Build web APIs with FastAPI.",
    },
    {
        "course_id": 3,
        "title": "Embedded Systems Fundamentals",
        "duration": "4 Weeks",
        "description": "An introduction to embedded applications.",
    },
    {
        "course_id": 4,
        "title": "Web Development",
        "duration": "4 Weeks",
        "description": "Build the structure and style of web pages.",
    },
    {
        "course_id": 5,
        "title": "Data Analysis with Python",
        "duration": "4 Weeks",
        "description": "Explore and summarize data in Python.",
    },
]

ENROLLMENTS = []
NEXT_ENROLLMENT_ID = 101


def find_course(course_id):
    for course in COURSES:
        if course["course_id"] == course_id:
            return course
    return None


def find_enrollment(enrollment_id):
    for record in ENROLLMENTS:
        if record["enrollment_id"] == enrollment_id:
            return record
    return None


def list_enrollments(course_id=None):
    if course_id is None:
        return ENROLLMENTS
    return [r for r in ENROLLMENTS if r["course_id"] == course_id]


def validate_enrollment_data(data):
    if not isinstance(data, dict):
        raise ValueError("Registration data must be a JSON object.")

    name = data.get("student_name")
    email = data.get("email")
    phone = data.get("phone")
    course_id = data.get("course_id")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name is required.")
    if not isinstance(email, str) or "@" not in email or not email.strip():
        raise ValueError("Enter a valid-looking email address.")
    if not isinstance(phone, str) or not phone.strip():
        raise ValueError("Phone number is required.")
    if type(course_id) is not int or find_course(course_id) is None:
        raise ValueError("Choose an existing course ID.")

    return {
        "student_name": name.strip(),
        "email": email.strip(),
        "phone": phone.strip(),
        "course_id": course_id,
    }


def add_enrollment(data):
    global NEXT_ENROLLMENT_ID
    fields = validate_enrollment_data(data)
    record = {"enrollment_id": NEXT_ENROLLMENT_ID, **fields}
    ENROLLMENTS.append(record)
    NEXT_ENROLLMENT_ID += 1
    return record


def update_enrollment(enrollment_id, data):
    record = find_enrollment(enrollment_id)
    if record is None:
        raise LookupError("Enrollment not found.")
    fields = validate_enrollment_data(data)
    record.update(fields)
    return record


def remove_enrollment(enrollment_id):
    record = find_enrollment(enrollment_id)
    if record is None:
        raise LookupError("Enrollment not found.")
    ENROLLMENTS.remove(record)
