"""Tests for add_word functionality."""
import pytest
from vocab_builder.features.add_word import word_exists


class TestAddWord:
    """Test add_word functionality."""
    
    def test_word_exists_case_insensitive(self):
        """Test that word_exists works case-insensitively."""
        vocab = {
            "words": [
                {"word": "Ephemeral", "pos": "adjective", "meaning": "lasting for a very short time"},
                {"word": "ubiquitous", "pos": "adjective", "meaning": "present everywhere"}
            ]
        }
        
        assert word_exists(vocab, "ephemeral") == True
        assert word_exists(vocab, "EPHEMERAL") == True
        assert word_exists(vocab, "Ubiquitous") == True
        assert word_exists(vocab, "nonexistent") == False
    
    @pytest.mark.skip(reason="TODO: Implement validation rules in Lesson 4")
    def test_collect_word_validation_rules(self):
        """Test that collect_word enforces validation rules.
        
        TODO: Implement this test after completing validation rules
        - word: 2–40 chars, letters and hyphen only (regex ^[A-Za-z-]+$)
        - pos: one of ["noun","verb","adjective","adverb","other"]
        - meaning: 3–160 chars
        - example: optional, 0–200 chars
        - tags: optional comma-separated → list[str] lowercased/trimmed
        """
        pass
