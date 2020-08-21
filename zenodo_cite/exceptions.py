"""Module with custom exceptions."""


class ZenodoLookupError(ValueError):
    """Exception thrown when the zenodo api doesn't find a matching doi or concept doi."""

    def __init__(self, doi: str) -> None:
        """Set error message for LookupError, adding the value of doi to it."""
        super().__init__(f"There was no entry at zenodo that had the doi or concept doi of: {doi}")


class MissingIdentifierException(ValueError):
    """Exception thrown when trying to generate a citation without a version."""

    def __init__(self) -> None:
        """Set error message for MissingIdentifierException."""
        super().__init__(
            "Neither 'doi' was provided, which makes it impossible to find the entry on Zenodo.\n"
            "Please provide the 'doi', either when initializing the Zenodo class "
            "or when calling a citation method."
        )
