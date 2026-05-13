from agent4ge.config import Settings


def test_settings_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.app_env == "local"
    assert settings.database_url is None
    assert settings.api_prefix == "/api/v1"
    assert settings.log_level == "INFO"


def test_settings_read_environment_variables(monkeypatch) -> None:
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")
    monkeypatch.setenv("API_PREFIX", "/api/test")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings(_env_file=None)

    assert settings.app_env == "test"
    assert settings.database_url == "sqlite:///test.db"
    assert settings.api_prefix == "/api/test"
    assert settings.log_level == "DEBUG"
