from src import channel
import unittest

class TestChannel(unittest.TestCase):

    base_channel = channel.Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    other_channel = channel.Channel('UCwHL6WHUarjGfUM_586me8w')

    def test_str(self):
        self.assertEqual(str(TestChannel.base_channel), TestChannel.base_channel.info)

    def test_add(self):
        summ = TestChannel.base_channel + TestChannel.other_channel
        self.assertEqual(summ, 100100)

if __name__ == '__main__':
    unittest.main()
