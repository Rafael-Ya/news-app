import os
import pytest # type: ignore
import app.news_scraper as news_scraper # type: ignore


@pytest.fixture
def mock_env_api_key(monkeypatch):
    monkeypatch.setenv("NEWS_API_KEY", "fake_api_key")


@pytest.fixture
def mock_no_api_key(monkeypatch):
    monkeypatch.delenv("NEWS_API_KEY", raising=False)

def test_news_fetching_with_api_key(mock_env_api_key):
    """Test if get_magnificent_seven_news runs without crashing when API key is present."""
    news = news_scraper.get_magnificent_seven_news()
    assert isinstance(news, list)  # Should return a list
    assert len(news) <= 50  # Should not return more than 50 items

def test_news_fetching_without_api_key(mock_no_api_key, caplog):
    """Test if get_magnificent_seven_news returns an empty list when API key is missing."""
    news = news_scraper.get_magnificent_seven_news()
    assert news == []  # Should return an empty list
    assert "NEWS_API_KEY is missing" in caplog.text  # Should log an error