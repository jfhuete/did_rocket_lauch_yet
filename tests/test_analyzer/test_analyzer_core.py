from unittest import TestCase
from src.did_rocket_launch_yet.analyzer.core import FrameXAnalyzer


class TestAnalyzerCore(TestCase):
    """
    Tests for analyzer core module
    """

    def setUp(self):
        self.firstFrame = 20
        self.lastFrame = 30
        self.actualFrame = 25
        self.analyzer = FrameXAnalyzer(
        first_frame=self.firstFrame,
        last_frame=self.lastFrame,
        actual_frame=self.actualFrame
        )

    def test_next_frame_for_is_launched_true(self):
        """
        Test next frame for is launched true
        """

        expected_actual_frame = 22
        expected_last_frame = 25
        expected_first_frame = 20

        self.analyzer.get_next_frame(is_launched=True)

        self.assertEqual(expected_first_frame, self.analyzer.first_frame)
        self.assertEqual(expected_last_frame, self.analyzer.last_frame)
        self.assertEqual(expected_actual_frame, self.analyzer.actual_frame)

    def test_next_frame_for_is_launched_false(self):
        """
        Test next frame for is launched false
        """

        expected_actual_frame = 28
        expected_last_frame = 30
        expected_first_frame = 25

        self.analyzer.get_next_frame(is_launched=False)

        self.assertEqual(expected_first_frame, self.analyzer.first_frame)
        self.assertEqual(expected_last_frame, self.analyzer.last_frame)
        self.assertEqual(expected_actual_frame, self.analyzer.actual_frame)

    def test_frame_found_actual_frame_equal_to_last_frame_or_first_frame(self):
        """
        Test frame found actual frame equal to last frame or first frame
        """

        analyzer = FrameXAnalyzer(
        first_frame=1,
        last_frame=2,
        actual_frame=1
        )

        self.assertTrue(analyzer.frame_found)

    def test_frame_found_actual_frame_in_middle_of_last_frame_and_first_frame(self):
        """
        Test frame found actual frame in middle of last frame and first frame
        """

        analyzer = FrameXAnalyzer(
        first_frame=1,
        last_frame=3,
        actual_frame=2
        )

        self.assertTrue(analyzer.frame_found)

    def test_instance_data_return_correct_values(self):
        """
        Test frame found actual frame in middle of last frame and first frame
        """

        expected_instance_data = {
            "actual_frame": self.analyzer.actual_frame,
            "last_frame": self.analyzer.last_frame,
            "first_frame": self.analyzer.first_frame
        }

        self.assertDictEqual(
            expected_instance_data,
            self.analyzer.instance_data
        )
