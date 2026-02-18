import unittest
from unittest.mock import patch
from employee import Employee


class test_employee(unittest.TestCase):
    def setUp(self):
        self.e1 = Employee('Lakshmanan', 'Palaniappan', 90000)
        self.e2 = Employee('Random', 'Person', 84000)

    def tearDown(self):
        print("tearDown\n")

    def test_email(self):

        self.assertEqual(self.e1.email(), 'Lakshmanan.Palaniappan@gmail.com')
        self.assertEqual(self.e2.email(), "Random.Person@gmail.com")

        self.e1.first = "Leo"
        self.e2.first = "Scorpion"

        self.assertEqual(self.e1.email(), "Leo.Palaniappan@gmail.com")
        self.assertEqual(self.e2.email(), "Scorpion.Person@gmail.com")

    def test_full_name(self):
        self.e1 = Employee('Lakshmanan', 'Palaniappan', 90000)
        self.e2 = Employee('Random', 'Person', 84000)

        self.assertEqual(self.e1.full_name(), "Lakshmanan Palaniappan")
        self.assertEqual(self.e2.full_name(), "Random Person")

    def test_pay_raise(self):
        self.e1 = Employee('Lakshmanan', 'Palaniappan', 90000)
        self.e2 = Employee('Random', 'Person', 84000)
        self.e1.raise_pay()
        self.e2.raise_pay()

        self.assertEqual(self.e1.pay, 94500)
        self.assertEqual(self.e2.pay, 88200)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = "Success"
            schedule = self.e1.monthly_schedule("June")
            mock_get.assert_called_with("http://server:port/Palaniappan/June")
            self.assertEqual(schedule, "Success")


if __name__ == "__main__":
    unittest.main()
