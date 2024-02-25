"""Rename RT Struct with a dict map."""
from pathlib import Path
from typing import Dict
from pydicom import dcmread

# ------------------------------------------------------------------------
def rename_structure_names(rtstruct_filename: Path, structure_name_mapper: Dict[str:str]):
    """"""
    rtstruct = dcmread(rtstruct_filename)
    structure_set_roi_sequence = rtstruct["StructureSetROISequence"]
    for structure_set_roi in structure_set_roi_sequence:
        structure_set_roi_name = structure_set_roi["ROIName"]
        structure_set_roi_name.value = structure_name_mapper(structure_set_roi_name.value.upper())
    rtstruct.save_as(rtstruct_filename)
