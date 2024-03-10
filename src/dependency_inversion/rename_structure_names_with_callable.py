""""""
from pathlib import Path
from typing import Callable, Union

from dependency_inversion.rtstruct_helpers import visit_roi_names


# ------------------------------------------------------------------------
def my_structure_name_mapper(value: str) -> Union[str, None]:
    """"""
    return None


# ------------------------------------------------------------------------
def rename_structure_names(rtstruct_filename: Path, structure_name_mapper: Callable):
    """"""
    for roi_name in visit_roi_names(rtstruct_filename):
        if new_value := structure_name_mapper(roi_name.value):
            roi_name.value = new_value
