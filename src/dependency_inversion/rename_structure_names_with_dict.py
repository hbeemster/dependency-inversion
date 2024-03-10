"""Rename RT Struct with a dict map."""
from pathlib import Path
from typing import Dict

from dependency_inversion.rtstruct_helpers import visit_roi_names


# ------------------------------------------------------------------------
def rename_structure_names(rtstruct_filename: Path, structure_name_mapper: Dict):
    """"""
    for roi_name in visit_roi_names(rtstruct_filename):
        if new_value := structure_name_mapper.get(roi_name.value):
            roi_name.value = new_value
