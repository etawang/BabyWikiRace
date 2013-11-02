import random
import unittest
import main
 
#main = imp.load_source('main', '../source/main.py')

class TestMain(unittest.TestCase):

    def setUp(self):
        self.startTopic = 'sailboat'

    def testReturnRandomLink(self):
        self.assertEqual(None, main.returnRandomLink([]))
        self.assertEqual('a', main.returnRandomLink(['a']))
        outputs = {}
        inputs = [str(x) for x in range(50)]
        for i in xrange(20):
            ret = main.returnRandomLink(inputs)
            if ret not in outputs.keys():
                outputs[ret] = 1
            else:
                outputs[ret] += 1
        self.assertTrue(len(outputs.keys()) > 10)

    def testGetTarget(self):
        self.assertEqual((self.startTopic, [self.startTopic]), 
            main.getTarget(self.startTopic, 0))

if __name__ == '__main__':
    unittest.main()
