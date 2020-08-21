"""Module with functions interfacing with the zenodo api.

For details see: https://developers.zenodo.org/#records

This module was strongly inspired by pyzenodo3
https://github.com/space-physics/pyzenodo3
"""
from typing import Any, Dict, List, Union

import requests

from zenodo_cite.exceptions import ZenodoLookupError


def get_record_by_doi(
    doi: str, is_version_doi=True, query_params: Dict[str, Union[int, str]] = {"size": 1}
) -> List[Dict[str, Any]]:
    """Retrieve a Record from the zenodo api, where doi or conceptdoi matches 'doi'.

    Parameters
    ----------
    doi : str
        Doi or concept doi, which should looked up at Zenodo.
    is_version_doi : bool, optional
        Whether 'doi' is a version doi or a concept doi, by default True
    query_params : Dict[str, Union[int, str]], optional
        Additional parameters for the request, by default {"size": 1}

    Returns
    -------
    Dict[str, Any]
        Result of the match query request
    """
    url_doi = doi.replace("/", "*")
    records_url = "https://zenodo.org/api/records"
    if is_version_doi:
        query_params["q"] = "doi:" + url_doi
    else:
        query_params["q"] = "conceptdoi:" + url_doi
    return requests.get(records_url, params=query_params).json()["hits"]["hits"]


def get_concept_doi(doi: str, is_concept_doi=False) -> str:
    """Retrieve concept doi from the zenodo api, if is_concept_doi is false.

    This is a helper function, if a user just provides a doi
    which might be the concept doi or the doi of a specific version.

    Parameters
    ----------
    doi : str
        Doi or concept doi, which should looked up at Zenodo.
    is_concept_doi : bool, optional
        Flag to intercept the lookup, by default False

    Raises
    ------
    LookupError
        If Neither a matching doi nor concept doi could be found.
    """
    if is_concept_doi:
        return doi
    else:
        for is_version_doi in [False, True]:
            result = get_record_by_doi(doi, is_version_doi)
            if len(result):
                return result[0]["conceptdoi"]
        raise ZenodoLookupError(doi)
