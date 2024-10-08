import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

if TYPE_CHECKING:
    from .request_extract_from_pdf import ExtractFromPDFRequest


T = TypeVar("T", bound="BodyExtractFromPdf")


@_attrs_define
class BodyExtractFromPdf:
    """
    Attributes:
        sec_req_extract (SecReqExtractFromPDFRequest):
        file (File):
    """

    sec_req_extract: "ExtractFromPDFRequest"
    file: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sec_req_extract = self.sec_req_extract.to_dict()

        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sec_req_extract": sec_req_extract,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        sec_req_extract = (
            None,
            json.dumps(self.sec_req_extract.to_dict()).encode(),
            "application/json",
        )

        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "sec_req_extract": sec_req_extract,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from .request_extract_from_pdf import (
            ExtractFromPDFRequest,
        )

        d = src_dict.copy()
        sec_req_extract = ExtractFromPDFRequest.from_dict(
            d.pop("sec_req_extract")
        )

        file = File(payload=BytesIO(d.pop("file")))

        body_post_sec_req_extract_from_pdf_api_tasks_sec_req_extract_from_pdf_post = (
            cls(
                sec_req_extract=sec_req_extract,
                file=file,
            )
        )

        body_post_sec_req_extract_from_pdf_api_tasks_sec_req_extract_from_pdf_post.additional_properties = (
            d
        )
        return (
            body_post_sec_req_extract_from_pdf_api_tasks_sec_req_extract_from_pdf_post
        )

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
