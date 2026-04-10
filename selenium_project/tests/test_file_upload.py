import pytest
from pathlib import Path


file_path = Path(__file__).parent.parent / "data/upload_file.txt"


@pytest.fixture
def uploaded_file(file_upload):
    file_upload.upload_file(str(file_path))
    return file_upload

def test_correct_file_selected(uploaded_file):
    """Verify file is selected."""
    assert Path(uploaded_file.get_uploaded_file()).name == file_path.name

def test_file_upload_success(file_upload):
    file_upload.upload_file(str(file_path))
    file_upload.tap_submit_btn()
    assert file_upload.is_file_submitted()

@pytest.mark.parametrize("expected_errors", [5])
def test_error_count_in_file(expected_errors):
    """Verify lines with ERROR."""
    num_error_lines=0
    with open(file_path, "r") as file:
        for line in file:
            if 'ERROR' in line:
                num_error_lines+=1
        assert num_error_lines == expected_errors
