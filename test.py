import random
import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.startTopic = 'sailboat'

    def testReturnRandomLink(self):
        self.assertEqual(None, returnRandomLink([]))
        self.assertEqual('a', returnRandomLink(['a']))
        outputs = {}
        inputs = [str(x) for x in range(50)]
        for i in xrange(20):
            ret = returnRandomLink(inputs)
            if ret not in outputs.keys():
                outputs[ret] = 1
            else:
                outputs[ret] += 1
        self.assertTrue(len(outputs.keys()) > 10)

    def testGetTarget(self):
        self.assertEqual([self.startTopic], getTarget(startTopic, 0))

if __name__ == '__main__':
    unittest.main()
