"""Tests for custom exceptions"""

import pytest

from zenodo_cite.exceptions import LookupError, MissingIdentifierException


def test_LookupError():
    doi = "this_is_a_doi"
    with pytest.raises(LookupError) as excinfo:
        raise LookupError(doi)
    assert doi in str(excinfo.value)


def test_MissingIdentifierException():
    with pytest.raises(MissingIdentifierException) as excinfo:
        raise MissingIdentifierException()
    assert str(excinfo.value).startswith("Neither 'doi'")
