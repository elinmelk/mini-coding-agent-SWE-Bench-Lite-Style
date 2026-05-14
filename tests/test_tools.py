"""Test tool suite"""

import pytest
import tempfile
import os
from src.agent.tools import ToolSuite


class TestToolSuite:
    """Test ToolSuite class"""

    def setup_method(self):
        """Setup test fixtures"""
        self.tools = ToolSuite()
        self.temp_dir = tempfile.mkdtemp()

    def test_read_file(self):
        """Test reading a file"""
        # Create test file
        test_file = os.path.join(self.temp_dir, "test.py")
        with open(test_file, "w") as f:
            f.write("print('hello')")
        
        result = self.tools.read_file(self.temp_dir, "test.py")
        assert result["success"]
        assert "hello" in result["content"]

    def test_list_directory(self):
        """Test listing directory"""
        # Create test files
        open(os.path.join(self.temp_dir, "file1.py"), "w").close()
        open(os.path.join(self.temp_dir, "file2.py"), "w").close()
        
        result = self.tools.list_directory(self.temp_dir)
        assert result["success"]
        assert len(result["items"]) >= 2

    def test_edit_file(self):
        """Test editing a file"""
        result = self.tools.edit_file(self.temp_dir, "new_file.py", "x = 1")
        assert result["success"]
        
        # Verify file was created
        with open(os.path.join(self.temp_dir, "new_file.py")) as f:
            assert f.read() == "x = 1"
