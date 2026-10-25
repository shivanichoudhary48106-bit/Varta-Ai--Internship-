import unittest

from src.workflow import WorkflowStep, sample_workflow, validate_step, validate_workflow


class WorkflowTests(unittest.TestCase):
    def test_matching_expected_and_actual_passes(self):
        step = WorkflowStep("Check input", "accepted", "accepted")
        result = validate_step(step)
        self.assertTrue(result.passed)

    def test_mismatch_fails(self):
        step = WorkflowStep("Check response", "success", "error")
        result = validate_step(step)
        self.assertFalse(result.passed)
        self.assertEqual(result.expected, "success")
        self.assertEqual(result.actual, "error")

    def test_sample_workflow_has_four_steps(self):
        self.assertEqual(len(sample_workflow()), 4)

    def test_sample_workflow_passes(self):
        results = validate_workflow(sample_workflow())
        self.assertTrue(all(result.passed for result in results))


if __name__ == "__main__":
    unittest.main()
