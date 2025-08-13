"""Tests for store utilities."""
import pytest
import tempfile
from pathlib import Path
from vocab_builder.utils.store import ensure_file, read_json, write_json, default_vocab, default_history


class TestStore:
    """Test store utility functions."""
    
    def test_ensure_file_creates_vocab_structure(self):
        """Test that ensure_file creates proper structure for vocab JSON."""
        with tempfile.TemporaryDirectory() as temp_dir:
            vocab_path = Path(temp_dir) / "vocab.json"
            ensure_file(vocab_path, default_vocab)
            
            assert vocab_path.exists()
            data = read_json(vocab_path)
            assert "meta" in data
            assert "words" in data
            assert data["meta"]["version"] == 1
            assert data["words"] == []
    
    def test_ensure_file_creates_history_structure(self):
        """Test that ensure_file creates proper structure for history JSON."""
        with tempfile.TemporaryDirectory() as temp_dir:
            history_path = Path(temp_dir) / "history.json"
            ensure_file(history_path, default_history)
            
            assert history_path.exists()
            data = read_json(history_path)
            assert "sessions" in data
            assert "wrong_bank" in data
            assert data["sessions"] == []
            assert data["wrong_bank"] == {}
    
    def test_write_json_read_json_roundtrip(self):
        """Test that write_json then read_json preserves data."""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_path = Path(temp_dir) / "test.json"
            test_data = {"test": "data", "numbers": [1, 2, 3]}
            
            write_json(test_path, test_data)
            assert test_path.exists()
            
            loaded_data = read_json(test_path)
            assert loaded_data == test_data
