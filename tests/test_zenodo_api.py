"""Tests for Zenodo Api calls"""
import json
from pathlib import Path
from typing import Any, Dict, Union

import pytest

from zenodo_cite.exceptions import ZenodoLookupError
from zenodo_cite.zenodo_api import get_concept_doi, get_record_by_doi

REPO_BASE = Path(__file__).parent.parent
TEST_DATA_BASE = REPO_BASE / "tests" / "data"


def clean_changing_result_entries(result: Dict[str, Any]):
    del result["updated"]
    del result["stats"]["unique_views"]
    del result["stats"]["version_views"]
    del result["stats"]["version_unique_views"]
    del result["stats"]["views"]


@pytest.mark.parametrize(
    "doi, is_version_doi, query_params",
    [
        ("10.5281/zenodo.3979792", True, {"size": 1}),
        ("10.5281/zenodo.3979791", False, {"size": 1, "sort": "-mostrecent"}),
    ],
)
def test_get_record_by_doi(
    doi: str, is_version_doi: bool, query_params: Dict[str, Union[int, str]]
):
    with open((TEST_DATA_BASE / "get_record_by_doi_test_data.txt")) as test_data:
        expected_result = json.load(test_data)[0]
        clean_changing_result_entries(expected_result)
    result = get_record_by_doi(doi, is_version_doi, query_params)[0]
    clean_changing_result_entries(result)
    assert result == expected_result


@pytest.mark.parametrize(
    "doi,is_concept_doi",
    (
        ("10.5281/zenodo.3979792", False),
        ("10.5281/zenodo.3979792", True),
        ("10.5281/zenodo.3979791", False),
        ("not_a_doi", False),
    ),
)
def test_get_concept_doi(doi: str, is_concept_doi: bool):
    if doi == "not_a_doi":
        with pytest.raises(ZenodoLookupError) as excinfo:
            get_concept_doi(doi, is_concept_doi)
            assert doi in str(excinfo.value)
    elif is_concept_doi:
        assert get_concept_doi(doi, is_concept_doi) == "10.5281/zenodo.3979792"
    else:
        assert get_concept_doi(doi, is_concept_doi) == "10.5281/zenodo.3979791"
