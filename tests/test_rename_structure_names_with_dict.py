from pathlib import Path

from dependency_inversion.rename_structure_names_with_dict import rename_structure_names
import pytest

from tests.conftest import rtstruct_has_roi_name, FIXTURE_DIR


@pytest.mark.datafiles(FIXTURE_DIR / "rtstruct-1.dcm")
def test_rename_structure_names(datafiles):
    original_roi_name = "BODY"
    new_roi_name = "Body"
    rtstruct_filename = datafiles / "rtstruct-1.dcm"
    structure_name_mapper = {original_roi_name: new_roi_name}
    rename_structure_names(rtstruct_filename, structure_name_mapper)
    assert rtstruct_has_roi_name(rtstruct_filename, new_roi_name), f"expected to find '{new_roi_name}'"
    assert not rtstruct_has_roi_name(rtstruct_filename, original_roi_name), f"not expected to find '{original_roi_name}'"
