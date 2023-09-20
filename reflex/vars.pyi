""" Generated with stubgen from mypy, then manually edited, do not regen."""

from _typeshed import Incomplete
from abc import ABC
from reflex import constants as constants
from reflex.base import Base as Base
from reflex.state import State as State
from reflex.utils import console as console, format as format, types as types
from types import FunctionType
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Set,
    Type,
    Union,
    _GenericAlias,  # type: ignore
)

USED_VARIABLES: Incomplete

def get_unique_variable_name() -> str: ...

class Var(ABC):
    name: str
    type_: Type
    state: str = ""
    is_local: bool = False
    is_string: bool = False
    @classmethod
    def create(
        cls, value: Any, is_local: bool = False, is_string: bool = False
    ) -> Optional[Var]: ...
    @classmethod
    def create_safe(
        cls, value: Any, is_local: bool = False, is_string: bool = False
    ) -> Var: ...
    @classmethod
    def __class_getitem__(cls, type_: str) -> _GenericAlias: ...
    def equals(self, other: Var) -> bool: ...
    def to_string(self) -> Var: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __getitem__(self, i: Any) -> Var: ...
    def __getattribute__(self, name: str) -> Var: ...
    def operation(
        self,
        op: str = ...,
        other: Optional[Var] = ...,
        type_: Optional[Type] = ...,
        flip: bool = ...,
        fn: Optional[str] = ...,
    ) -> Var: ...
    def compare(self, op: str, other: Var) -> Var: ...
    def __invert__(self) -> Var: ...
    def __neg__(self) -> Var: ...
    def __abs__(self) -> Var: ...
    def length(self) -> Var: ...
    def __eq__(self, other: Var) -> Var: ...
    def __ne__(self, other: Var) -> Var: ...
    def __gt__(self, other: Var) -> Var: ...
    def __ge__(self, other: Var) -> Var: ...
    def __lt__(self, other: Var) -> Var: ...
    def __le__(self, other: Var) -> Var: ...
    def __add__(self, other: Var) -> Var: ...
    def __radd__(self, other: Var) -> Var: ...
    def __sub__(self, other: Var) -> Var: ...
    def __rsub__(self, other: Var) -> Var: ...
    def __mul__(self, other: Var) -> Var: ...
    def __rmul__(self, other: Var) -> Var: ...
    def __pow__(self, other: Var) -> Var: ...
    def __rpow__(self, other: Var) -> Var: ...
    def __truediv__(self, other: Var) -> Var: ...
    def __rtruediv__(self, other: Var) -> Var: ...
    def __floordiv__(self, other: Var) -> Var: ...
    def __mod__(self, other: Var) -> Var: ...
    def __rmod__(self, other: Var) -> Var: ...
    def __and__(self, other: Var) -> Var: ...
    def __rand__(self, other: Var) -> Var: ...
    def __or__(self, other: Var) -> Var: ...
    def __ror__(self, other: Var) -> Var: ...
    def __contains__(self, _: Any) -> Var: ...
    def contains(self, other: Any) -> Var: ...
    def reverse(self) -> Var: ...
    def foreach(self, fn: Callable) -> Var: ...
    def to(self, type_: Type) -> Var: ...
    @property
    def full_name(self) -> str: ...
    def set_state(self, state: Type[State]) -> Any: ...

class BaseVar(Var, Base):
    name: str
    type_: Any
    state: str = ""
    is_local: bool = False
    is_string: bool = False
    def __hash__(self) -> int: ...
    def get_default_value(self) -> Any: ...
    def get_setter_name(self, include_state: bool = ...) -> str: ...
    def get_setter(self) -> Callable[[State, Any], None]: ...

class ComputedVar(Var):
    cache: bool
    @property
    def name(self) -> str: ...
    @property
    def cache_attr(self) -> str: ...
    def __get__(self, instance, owner): ...
    def deps(self, objclass: Type, obj: Optional[FunctionType] = ...) -> Set[str]: ...
    def mark_dirty(self, instance) -> None: ...
    @property
    def type_(self): ...
    def __init__(self, func) -> None: ...

def cached_var(fget: Callable[[Any], Any]) -> ComputedVar: ...

class ImportVar(Base):
    tag: Optional[str]
    is_default: Optional[bool] = False
    alias: Optional[str] = None
    @property
    def name(self) -> str: ...
    def __hash__(self) -> int: ...

class NoRenderImportVar(ImportVar):
    """A import that doesn't need to be rendered."""

def get_local_storage(key: Optional[Union[Var, str]] = ...) -> BaseVar: ...
