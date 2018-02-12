import unittest


class TestDemo(unittest.TestCase):

    def test_upper(self):
        self.assertTrue('ABC'.isupper())
        self.assertFalse('abc'.isupper())
        with self.assertRaises(KeyError):
            d = {'a': 1}
            print(d['b'])

    def test_equal(self):
        self.assertEqual('abc'.upper(), 'a')


# unittest.main()
# suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
# unittest.TextTestRunner(verbosity=2).run(suite)
