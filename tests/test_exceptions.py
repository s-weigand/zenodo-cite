"""Tests for custom exceptions"""

import pytest

from zenodo_cite.exceptions import MissingIdentifierException, ZenodoLookupError


def test_LookupError():
    doi = "this_is_a_doi"
    with pytest.raises(ZenodoLookupError) as excinfo:
        raise ZenodoLookupError(doi)
    assert doi in str(excinfo.value)


def test_MissingIdentifierException():
    with pytest.raises(MissingIdentifierException) as excinfo:
        raise MissingIdentifierException()
    assert str(excinfo.value).startswith("Neither 'doi'")
