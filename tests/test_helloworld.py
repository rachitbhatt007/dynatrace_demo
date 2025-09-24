import pytest
import io
import contextlib
import sys
import os

# Add the root directory to Python path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from core.helloworld import hello_world

class TestHelloWorld:
    """Test cases for helloWorld.py functions"""
    
    def test_hello_world_return_value(self):
        """Test that hello_world returns the correct string"""
        # Act
        result = hello_world()
        
        # Assert
        assert result == "Hello, World!"
        assert isinstance(result, str)
    
    def test_hello_world_output(self):
        """Test that hello_world prints the correct message"""
        # Arrange
        expected_output = "Hello, World!\n"
        
        # Act & Assert
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            hello_world()
        output = f.getvalue()
        
        assert output == expected_output
    
    def test_hello_world_no_errors(self):
        """Test that hello_world runs without errors"""
        # This test ensures the function doesn't raise any exceptions
        try:
            result = hello_world()
            assert result is not None
        except Exception as e:
            pytest.fail(f"hello_world raised an exception: {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])