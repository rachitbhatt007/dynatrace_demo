import pytest
import io
import contextlib
import sys
import os

# Add the root directory to Python path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from utilities.sf_connect import snowflake_connect, snowflake_disconnect

class TestSnowflakeConnect:
    """Test cases for sf_connect.py functions"""
    
    def test_snowflake_connect_return_value(self):
        """Test that snowflake_connect returns correct dictionary"""
        # Act
        result = snowflake_connect()
        
        # Assert
        assert isinstance(result, dict)
        assert "status" in result
        assert result["status"] == "connected"
        assert len(result) == 1  # Only status key should be present
    
    def test_snowflake_connect_output(self):
        """Test that snowflake_connect prints correct message"""
        # Arrange
        expected_output = "Connecting to Snowflake...\n"
        
        # Act & Assert
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = snowflake_connect()
        output = f.getvalue()
        
        assert output == expected_output
        assert result["status"] == "connected"
    
    def test_snowflake_disconnect_return_value(self):
        """Test that snowflake_disconnect returns correct dictionary"""
        # Act
        result = snowflake_disconnect()
        
        # Assert
        assert isinstance(result, dict)
        assert "status" in result
        assert result["status"] == "disconnected"
        assert len(result) == 1
    
    def test_snowflake_disconnect_output(self):
        """Test that snowflake_disconnect prints correct message"""
        # Arrange
        expected_output = "Disconnecting from Snowflake...\n"
        
        # Act & Assert
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = snowflake_disconnect()
        output = f.getvalue()
        
        assert output == expected_output
        assert result["status"] == "disconnected"
    
    def test_functions_independent(self):
        """Test that connect and disconnect work independently"""
        # This test ensures they don't share state incorrectly
        
        # Test connect
        connect_result = snowflake_connect()
        assert connect_result["status"] == "connected"
        
        # Test disconnect
        disconnect_result = snowflake_disconnect()
        assert disconnect_result["status"] == "disconnected"
        
        # Test connect again to ensure no side effects
        connect_result2 = snowflake_connect()
        assert connect_result2["status"] == "connected"
    
    def test_function_signatures(self):
        """Test that functions have correct signatures"""
        import inspect
        
        # Test snowflake_connect signature
        connect_sig = inspect.signature(snowflake_connect)
        assert len(connect_sig.parameters) == 0  # No parameters
        
        # Test snowflake_disconnect signature
        disconnect_sig = inspect.signature(snowflake_disconnect)
        assert len(disconnect_sig.parameters) == 0  # No parameters
    
    def test_no_exceptions_raised(self):
        """Test that functions don't raise exceptions"""
        try:
            result1 = snowflake_connect()
            result2 = snowflake_disconnect()
            assert result1 is not None
            assert result2 is not None
        except Exception as e:
            pytest.fail(f"Functions raised an exception: {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])