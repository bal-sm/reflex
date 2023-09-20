"""Stub file for circularprogress.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, Union, overload
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class CircularProgress(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, label, cap_is_round: Optional[Union[Var[bool], bool]] = None, is_indeterminate: Optional[Union[Var[bool], bool]] = None, max_: Optional[Union[Var[int], int]] = None, min_: Optional[Union[Var[int], int]] = None, thickness: Optional[Union[Var[int], int]] = None, track_color: Optional[Union[Var[str], str]] = None, value: Optional[Union[Var[int], int]] = None, value_text: Optional[Union[Var[str], str]] = None, color: Optional[Union[Var[str], str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "CircularProgress":  # type: ignore
        """Create a circular progress component.

        Args:
            *children: the children of the component.
            cap_is_round: If true, the cap of the progress indicator will be rounded.
            is_indeterminate: If true, the progress will be indeterminate and the value prop will be ignored
            max_: Maximum value defining 100% progress made (must be higher than 'min')
            min_: Minimum value defining 'no progress' (must be lower than 'max')
            thickness: This defines the stroke width of the svg circle.
            track_color: The color name of the progress track. Use a color key in the theme object
            value: Current progress (must be between min/max).
            value_text: The desired valueText to use in place of the value.
            color: The color name of the progress bar
            label: A label to add in the circular progress. Defaults to None.
            **props: the props of the component.

        Returns:
            The circular progress component.
        """
        ...

class CircularProgressLabel(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "CircularProgressLabel":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
