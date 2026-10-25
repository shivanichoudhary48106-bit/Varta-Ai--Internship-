"""A small, generic workflow and validation demo.

This is sample code created for portfolio demonstration. It is not Varta AI's
original implementation.
"""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class WorkflowStep:
    name: str
    expected: str
    actual: str


@dataclass(frozen=True)
class StepResult:
    name: str
    passed: bool
    expected: str
    actual: str


def validate_step(step: WorkflowStep) -> StepResult:
    """Compare actual and expected outcomes for one workflow step."""
    return StepResult(
        name=step.name,
        passed=step.actual == step.expected,
        expected=step.expected,
        actual=step.actual,
    )


def validate_workflow(steps: Iterable[WorkflowStep]) -> list[StepResult]:
    """Validate each step and return a result for every step."""
    return [validate_step(step) for step in steps]


def sample_workflow() -> list[WorkflowStep]:
    """Return illustrative steps for a generic request-response workflow."""
    return [
        WorkflowStep("Open application", "application_open", "application_open"),
        WorkflowStep("Enter valid input", "input_accepted", "input_accepted"),
        WorkflowStep("Process request", "request_processed", "request_processed"),
        WorkflowStep("Display response", "response_displayed", "response_displayed"),
    ]


def main() -> None:
    steps = sample_workflow()
    results = validate_workflow(steps)

    print("Workflow: Sample Varta AI Flow")
    print(f"Steps: {len(results)}")
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} - {result.name}")
        if not result.passed:
            print(f"  Expected: {result.expected}")
            print(f"  Actual:   {result.actual}")

    overall = all(result.passed for result in results)
    print(f"Result: {'PASS' if overall else 'FAIL'}")


if __name__ == "__main__":
    main()
