from unittest import TestCase
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student(name="Timur", courses=None)

    def test_init(self):
        self.assertEqual("Timur", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        student = Student("Timur", {"Java": ["if_else", "loops"]})
        self.assertEqual("Timur", student.name)
        self.assertEqual({"Java": ["if_else", "loops"]}, student.courses)

    def test_course_is_already_present(self):
        self.student.courses = {"Python": ["loops"]}
        res = self.student.enroll("Python", ["lists"], "")
        new_dict = {"Python": ["loops", "lists"]}
        result = "Course already added. Notes have been updated."
        self.assertEqual(result, res)
        self.assertEqual(new_dict, self.student.courses)

    def test_add_new_course_and_Y(self):
        self.student.courses = {"Python": ["loops"]}
        res = self.student.enroll("Java", ["loops"], "Y")
        new_dict = {"Python": ["loops"], "Java": ["loops"]}
        result = "Course and course notes have been added."
        self.assertEqual(result, res)
        self.assertEqual(new_dict, self.student.courses)

    def test_add_new_course_and_empty_str(self):
        self.student.courses = {"Python": ["loops"]}
        res = self.student.enroll("Java", ["loops"], "")
        new_dict = {"Python": ["loops"], "Java": ["loops"]}
        result = "Course and course notes have been added."
        self.assertEqual(result, res)
        self.assertEqual(new_dict, self.student.courses)

    def test_add_course_to_empty_dict(self):
        res = self.student.enroll("Java", ["loops"], "No")
        new_dict = {"Java": []}
        result = "Course has been added."
        self.assertEqual(result, res)
        self.assertEqual(new_dict, self.student.courses)

    def test_add_notes_to_existing_course(self):
        self.student.courses = {"Python": ["loops"]}
        res = self.student.add_notes("Python", "if_else")
        new_dict = {"Python": ["loops", "if_else"]}
        result = "Notes have been updated"
        self.assertEqual(result, res)
        self.assertEqual(new_dict, self.student.courses)

    def test_test_add_notes_to_not_existing_course(self):
        self.student.courses = {"Python": ["loops"]}
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", "loops")
            self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        self.student.courses = {"Python": ["loops"], "Java": ["loops"]}
        res = self.student.leave_course("Java")
        result = "Course has been removed"
        new_dict = {"Python": ["loops"]}
        self.assertEqual(result, res)
        self.assertEqual(new_dict, self.student.courses)

    def test_leave_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")
            self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))











