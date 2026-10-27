import unittest

from society_dues import add_due, collect, create_connection, penalty, pending


class SocietyDuesTests(unittest.TestCase):
    def setUp(self):
        self.connection = create_connection()

    def tearDown(self):
        self.connection.close()

    def test_add_due_and_history(self):
        history = add_due(self.connection, "A-101", "Oct", 2500)
        self.assertEqual(history, [("A-101", "Oct")])
        self.assertEqual(pending(self.connection), ["A-101"])

    def test_parameterized_values_allow_quotes(self):
        add_due(self.connection, "A'101", "Oct", 100)
        self.assertEqual(pending(self.connection), ["A'101"])

    def test_collect_marks_paid_and_returns_amount(self):
        add_due(self.connection, "A-101", "Oct", 2500)
        self.assertEqual(collect(self.connection, "A-101", "Oct"), 2500)
        self.assertEqual(pending(self.connection), [])

    def test_collect_missing_due(self):
        self.assertIsNone(collect(self.connection, "A-404", "Oct"))

    def test_penalty(self):
        self.assertEqual(penalty(50, 2), 100)

    def test_negative_amount_rejected(self):
        with self.assertRaises(ValueError):
            add_due(self.connection, "A-101", "Oct", -1)

    def test_negative_penalty_rejected(self):
        with self.assertRaises(ValueError):
            penalty(50, -2)


if __name__ == "__main__":
    unittest.main()
