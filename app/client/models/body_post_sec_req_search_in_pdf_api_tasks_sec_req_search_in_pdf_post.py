import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

if TYPE_CHECKING:
    from ..models.sec_req_search_in_pdf_request import SecReqSearchInPDFRequest


T = TypeVar("T", bound="BodyPostSecReqSearchInPdfApiTasksSecReqSearchInPdfPost")


@_attrs_define
class BodyPostSecReqSearchInPdfApiTasksSecReqSearchInPdfPost:
    """
    Attributes:
        sec_req_search (SecReqSearchInPDFRequest):
        file (File):
    """

    sec_req_search: "SecReqSearchInPDFRequest"
    file: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sec_req_search = self.sec_req_search.to_dict()

        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sec_req_search": sec_req_search,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        sec_req_search = (None, json.dumps(self.sec_req_search.to_dict()).encode(), "application/json")

        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "sec_req_search": sec_req_search,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sec_req_search_in_pdf_request import SecReqSearchInPDFRequest

        d = src_dict.copy()
        sec_req_search = SecReqSearchInPDFRequest.from_dict(d.pop("sec_req_search"))

        file = File(payload=BytesIO(d.pop("file")))

        body_post_sec_req_search_in_pdf_api_tasks_sec_req_search_in_pdf_post = cls(
            sec_req_search=sec_req_search,
            file=file,
        )

        body_post_sec_req_search_in_pdf_api_tasks_sec_req_search_in_pdf_post.additional_properties = d
        return body_post_sec_req_search_in_pdf_api_tasks_sec_req_search_in_pdf_post

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
