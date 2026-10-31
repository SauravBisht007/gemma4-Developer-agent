def compute_metric(success: int, total: int) -> float:
    if total == 0:
        return 0.0
    return success / total

if __name__ == "__main__":
    assert compute_metric(10, 20) == 0.5
    assert compute_metric(0, 0) == 0.0
    print("All mock tests passed successfully!")