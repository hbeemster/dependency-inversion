from pathlib import Path
from pydicom import dcmread
import pytest


FIXTURE_DIR = Path(__file__).parent / "data"


def roi_names_from_rtstruct(rtstruct_filename: Path) -> str:
    rtstruct = dcmread(rtstruct_filename)
    structure_set_roi_sequence = rtstruct["StructureSetROISequence"]
    for structure_set_roi in structure_set_roi_sequence:
        structure_set_roi_name = structure_set_roi["ROIName"]
        yield structure_set_roi_name.value


def rtstruct_has_roi_name(rtstruct_filename: Path, roi_name: str) -> bool:
    return roi_name in list(roi_names_from_rtstruct(rtstruct_filename))
