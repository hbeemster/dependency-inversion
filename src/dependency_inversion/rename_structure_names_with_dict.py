"""Rename RT Struct with a dict map."""
from pathlib import Path
from typing import Dict
from pydicom import dcmread

# ------------------------------------------------------------------------
def rename_structure_names(rtstruct_filename: Path, structure_name_mapper: Dict):
    """"""
    rtstruct = dcmread(rtstruct_filename)
    structure_set_roi_sequence = rtstruct["StructureSetROISequence"]
    for structure_set_roi in structure_set_roi_sequence:
        structure_set_roi_name = structure_set_roi["ROIName"]
        if new_value := structure_name_mapper.get(structure_set_roi_name.value):
            structure_set_roi_name.value = new_value
    rtstruct.save_as(rtstruct_filename)
