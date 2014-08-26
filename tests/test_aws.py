import unittest
from awacs.aws import Action

class TestAction(unittest.TestCase):
    def test_global_wildcard(self):
        action = Action('*')
        self.assertEqual(action.JSONrepr(), '*')

    def test_action_wildcard(self):
        action = Action('ec2', '*')
        self.assertEqual(action.JSONrepr(), 'ec2:*')

    def test_prefix_wildcard(self):
        with self.assertRaisesRegexp(ValueError, "^Action not supported with wildcard prefix$"):
            action = Action('*', 'DescribeInstances')

    def test_action_embedded_wildcard(self):
        action = Action('ec2', 'Describe*')
        self.assertEqual(action.JSONrepr(), 'ec2:Describe*')

if __name__ == '__main__':
    unittest.main()
