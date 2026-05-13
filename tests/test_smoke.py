from agent4ge.main import main


def test_main_runs_without_crashing() -> None:
    assert main() == 0
