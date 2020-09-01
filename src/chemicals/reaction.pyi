# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from pandas.core.frame import DataFrame
from typing import (
    Dict,
    List,
    Optional,
    Union,
)


def Gibbs_formation(
    dHf: float,
    S0_abs: float,
    dHfs_std: Union[List[float], List[float]],
    S0_abs_elements: List[float],
    coeffs_elements: Union[List[float], List[float]],
    T_ref: float = ...
) -> float: ...


def Hf_basis_converter(
    Hvapm: Optional[float],
    Hf_liq: Optional[float] = ...,
    Hf_gas: Optional[float] = ...
) -> float: ...


def Hfg(CASRN: str, method: Optional[str] = ...) -> Optional[float]: ...


def Hfg_methods(CASRN: str) -> List[str]: ...


def Hfl(CASRN: str, method: Optional[str] = ...) -> Optional[float]: ...


def Hfl_methods(CASRN: str) -> List[str]: ...


def Hfs(CASRN: str, method: Optional[str] = ...) -> float: ...


def Hfs_methods(CASRN: str) -> List[str]: ...


def S0g(CASRN: str, method: Optional[str] = ...) -> float: ...


def S0g_methods(CASRN: str) -> List[str]: ...


def S0l(CASRN: str, method: Optional[str] = ...) -> float: ...


def S0l_methods(CASRN: str) -> List[str]: ...


def S0s(CASRN: str, method: Optional[str] = ...) -> float: ...


def S0s_methods(CASRN: str) -> List[str]: ...


def __getattr__(name: str) -> DataFrame: ...


def _load_reaction_data() -> None: ...


def balance_stoichiometry(matrix: List[List[int]], rounding: int = ..., allow_fractional: bool = ...) -> List[float]: ...


def entropy_formation(Hf: float, Gf: float, T_ref: float = ...) -> float: ...


def stoichiometric_matrix(atomss: List[Dict[str, int]], reactants: List[bool]) -> List[List[int]]: ...

__all__: List[str]