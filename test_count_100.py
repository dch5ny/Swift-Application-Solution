import unittest
import count_100 as test


class MyTest(unittest.TestCase):
    
    def test_countFunc0(self):
        """
        Tests what the value of zero returns.
        Passes if a count of 0 prints "Fizz Buzz"

        """

        return self.assertEqual(test.countFunc(0), "Fizz Buzz")

    def test_countFunc3(self):
        """
        Tests what the value of a multiple of 3 returns.
        Passes if a count of 9 prints "Fizz"

        """

        return self.assertEqual(test.countFunc(9), "Fizz")

    def test_countFunc5(self):
        """
        Tests what the value of a multiple of 5 returns
        Passes if a count of 50 prints "Buzz"

        """

        return self.assertEqual(test.countFunc(50), "Buzz")

    def test_countFuncBoth(self):
        """
        Tests what the value of a multiple of both 3 and 5 returns
        Passes if a count of 15 prints "Fizz Buzz"

        """

        return self.assertEqual(test.countFunc(15), "Fizz Buzz")

    def test_countFuncNeither(self):
        """
        Tests what the value of a prime number returns
        Passes if a count of 23 returns the count value (23)

        """

        return self.assertEqual(test.countFunc(23), 23)

    def test_list(self):
        """
        Makes sure the program returns a value for all counts
        Passes if there are 101 items in the list (0-100)

        """

        y = [test.countFunc(x) for x in xrange(101)]
        return self.assertEqual(len(y), 101)

    def test_fullCount5(self):
        """
        Compares the output for multiples of five, with the expected value of 21.
        Passes if the solution contains "Buzz" 21 times

        """

        z = [test.countFunc(x) for x in xrange(101)]
        return self.assertEqual(z.count("Buzz") + z.count("Fizz Buzz"), 21)

if __name__ == '__main__':
    unittest.main()
