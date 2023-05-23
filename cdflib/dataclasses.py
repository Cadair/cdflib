from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Union

import numpy as np

__all__ = ["ADRInfo", "CDFInfo", "CDRInfo", "GDRInfo", "VDRInfo", "AEDR", "VDR", "AEDR", "AttData"]


@dataclass
class ADRInfo:
    scope: int
    next_adr_loc: int
    attribute_number: int
    num_gr_entry: int
    max_gr_entry: int
    num_z_entry: int
    max_z_entry: int
    first_z_entry: int
    first_gr_entry: int
    name: str


@dataclass
class CDFInfo:
    """
    CDF information.
    """

    #: Path to the CDF.
    CDF: Union[str, Path]
    #: CDF version.
    Version: str
    #: Endianness of the CDF.
    Encoding: int
    #: Row/column majority.
    Majority: str
    #: zVariable names.
    rVariables: List[str]
    #: rVariable names.
    zVariables: List[str]
    #: List of dictionary objects that map attribute_name to scope.
    Attributes: List[Dict[str, str]]
    Copyright: str
    #: Checksum indicator.
    Checksum: bool
    #: Number of dimensions for rVariables.
    Num_rdim: int
    #: Dimensional sizes for rVariables.
    rDim_sizes: List[int]
    #: If CDF is compressed at file level.
    Compressed: bool
    #: Last updated leap second table.
    LeapSecondUpdate: Optional[int] = None


@dataclass
class CDRInfo:
    encoding: int
    copyright_: str
    version: str
    majority: int
    format_: bool
    md5: bool
    post25: bool


@dataclass
class GDRInfo:
    first_zvariable: int
    first_rvariable: int
    first_adr: int
    num_zvariables: int
    num_rvariables: int
    num_attributes: int
    rvariables_num_dims: int
    rvariables_dim_sizes: List[int]
    eof: int
    leapsecond_updated: Optional[int] = None


@dataclass
class VDRInfo:
    """
    Variable data record info.
    """

    Variable: str
    Num: int
    Var_Type: str
    Data_Type: int
    Data_Type_Description: str
    Num_Elements: int
    Num_Dims: int
    Dim_Sizes: List[int]
    Sparse: str
    Last_Rec: int
    Rec_Vary: int
    Dim_Vary: Union[List[int], List[bool]]  #: a doc
    Compress: int
    Pad: Optional[int] = None
    Block_Factor: Optional[int] = None


@dataclass
class AEDR:
    entry: np.ndarray
    data_type: int
    num_elements: int
    next_aedr: int
    entry_num: int
    num_strings: Optional[int] = None


@dataclass
class VDR:
    data_type: int
    section_type: int
    next_vdr_location: int
    variable_number: int
    head_vxr: int
    last_vxr: int
    max_rec: int
    name: str
    num_dims: int
    dim_sizes: List[int]
    compression_bool: bool
    compression_level: int
    blocking_factor: int
    dim_vary: Union[List[int], List[bool]]
    record_vary: int
    num_elements: int
    sparse: int
    pad: Optional[bool] = None


@dataclass
class AttData:
    """
    Attribute data.
    """

    #: Number of bytes for each entry value.
    Item_Size: int
    #: CDF data type.
    Data_Type: str
    #: Number of values extracted.
    Num_Items: int
    #: Data as a scalar value, a numpy array or a string.
    Data: np.ndarray
