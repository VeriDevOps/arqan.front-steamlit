from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchDBRequest")


@_attrs_define
class SearchDBRequest:
    """
    Attributes:
        text (str):
        limit (Union[Unset, int]):  Default: 10.
        platform (Union[Unset, str]):
        source (Union[Unset, str]):
    """

    text: str
    limit: Union[Unset, int] = 10
    platform: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        limit = self.limit

        platform = self.platform

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if platform is not UNSET:
            field_dict["platform"] = platform
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        limit = d.pop("limit", UNSET)

        platform = d.pop("platform", UNSET)

        source = d.pop("source", UNSET)

        sec_req_search_db_request = cls(
            text=text,
            limit=limit,
            platform=platform,
            source=source,
        )

        sec_req_search_db_request.additional_properties = d
        return sec_req_search_db_request

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
