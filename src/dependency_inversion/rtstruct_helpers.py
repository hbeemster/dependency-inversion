from pathlib import Path

from pydicom import Dataset, dcmread


# ------------------------------------------------------------------------
def visit_roi_names(rtstruct_filename: Path) -> Dataset:
    rtstruct = dcmread(rtstruct_filename)
    structure_set_roi_sequence = rtstruct["StructureSetROISequence"]
    for structure_set_roi in structure_set_roi_sequence:
        yield structure_set_roi["ROIName"]
    rtstruct.save_as(rtstruct_filename)
