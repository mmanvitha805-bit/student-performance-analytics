import unittest
import pandas as pd


class TestStudentProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv("students.csv")

    def test_dataset_not_empty(self):
        self.assertGreater(len(self.df), 0)

    def test_required_columns_exist(self):
        required = [
            "student_id",
            "math_marks",
            "physics_marks",
            "programming_marks",
            "attendance",
            "previous_score"
        ]
        for column in required:
            self.assertIn(column, self.df.columns)

    def test_no_missing_values(self):
        self.assertFalse(self.df.isnull().any().any())

    def test_marks_are_in_valid_range(self):
        columns = [
            "math_marks",
            "physics_marks",
            "programming_marks",
            "attendance",
            "previous_score"
        ]
        for column in columns:
            self.assertTrue(self.df[column].between(0, 100).all())

    def test_student_ids_are_unique(self):
        self.assertEqual(
            self.df["student_id"].nunique(),
            len(self.df)
        )

    def test_average_calculation(self):
        first_student = self.df.iloc[0]
        expected = (
            first_student["math_marks"]
            + first_student["physics_marks"]
            + first_student["programming_marks"]
        ) / 3

        actual = sum([
            first_student["math_marks"],
            first_student["physics_marks"],
            first_student["programming_marks"]
        ]) / 3

        self.assertAlmostEqual(actual, expected, places=2)


if __name__ == "__main__":
    unittest.main()