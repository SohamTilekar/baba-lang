"""Basic errors"""


from .base import BLError

# pylint: disable=unused-import
from .base import error_not_implemented, error_div_by_zero  # noqa: F401


error_out_of_range = BLError("Index out of range: {}")
error_key_nonexistent = BLError("Non-existent key: {}")
error_var_nonexistent = BLError("Variable {} is undefined")
error_wrong_argc = BLError("Function {} needs exactly {} arguments")
error_module_var_nonexistent = BLError("Module {} doesn't have variable {}")
error_include_syntax = BLError("Error in include's syntax:\n{}")
error_inside_include = BLError(
    "Error inside include at line {}, column {}: {}"
)
error_invalid_include = BLError("Invalid include '{}'")