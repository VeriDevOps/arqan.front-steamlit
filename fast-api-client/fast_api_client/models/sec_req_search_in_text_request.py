from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecReqSearchInTextRequest")


@_attrs_define
class SecReqSearchInTextRequest:
    """
    Attributes:
        text (str):
        requirements (str):
        limit (Union[Unset, int]):  Default: 10.
    """

    text: str
    requirements: str
    limit: Union[Unset, int] = 10
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        requirements = self.requirements

        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "requirements": requirements,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        requirements = d.pop("requirements")

        limit = d.pop("limit", UNSET)

        sec_req_search_in_text_request = cls(
            text=text,
            requirements=requirements,
            limit=limit,
        )

        sec_req_search_in_text_request.additional_properties = d
        return sec_req_search_in_text_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
