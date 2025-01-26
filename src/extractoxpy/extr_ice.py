import requests
import numpy as np
from rich.console import Console
from typing import List, Optional
import pandas as pd
from .checks.internet import check_internet

console = Console()


def extr_ice(
    casrn: List[str],
    assays: Optional[List[str]] = None,
    verify_ssl: bool = False,
    verbose: bool = True,
    **kwargs,
) -> pd.DataFrame:
    """
    Extract Data from NTP ICE Database.

    The `extr_ice` function sends a POST request to the ICE API to search for
    information based on specified chemical IDs and assays.

    Parameters:
    - casrn: A list of CASRNs for the search.
    - assays: A list of assays to include in the search. Default is None, meaning all assays are included.
    - verify_ssl: Boolean to control if SSL should be verified or not.
    - verbose: A boolean indicating whether to print detailed messages. Default is True.
    - **kwargs: Any other arguments to be supplied to `requests.request` and thus to `libcurl`.

    Returns:
    A pandas DataFrame containing the extracted data from the ICE API.

    Raises:
    - ImportError: If the required dependencies are missing.
    - requests.RequestException: If there's an error during the request.
    - ValueError: If the CASRN argument is missing.

    See Also:
    - `extr_ice_assay_names()`: Function to search for assay names that match a pattern.
    - https://ice.ntp.niehs.nih.gov/: NTP ICE database
    """

    if not casrn:
        raise ValueError("The argument 'casrn' is required.")

    base_url = "https://ice.ntp.niehs.nih.gov/api/v1/search"

    if not isinstance(casrn, list):
        casrn = [casrn]

    if assays is not None and not isinstance(assays, list):
        assays = [assays]

    payload = {"chemids": casrn, "assays": assays}

    try:
        response = requests.post(url=base_url, json=payload)
    except requests.exceptions.ConnectionError as e:
        # Check if the internet connection is available
        check_internet()
        print(f"Connection Error:\n{e}")
        raise
    except requests.exceptions.Timeout as e:
        check_internet()
        print(f"Timeout occurred:\n {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Request Exception occurred:\n {e}")
        raise

    # the bella ciao case goes that if nothing it is retrieved an exception is raised.
    # that is not good
    col_names = [
        "assay",
        "endpoint",
        "substance_type",
        "casrn",
        "qsar_ready_id",
        "value",
        "unit",
        "species",
        "receptor_species",
        "route",
        "sex",
        "strain",
        "life_stage",
        "tissue",
        "lesion",
        "location",
        "assay_source",
        "in_vitro_assay_format",
        "reference",
        "reference_url",
        "dtxsid",
        "substance_name",
        "pubmed_id",
    ]

    if "CASRN not found or no results found" in response.text:
        dat_cl = pd.DataFrame(columns=col_names)
    else:
        dat = response.json()
        dat_cl = pd.DataFrame(dat["endPoints"])
        dat_cl.columns = col_names

    casrn_array = np.array(casrn)
    ids_not_found = casrn_array[~np.isin(casrn_array, dat_cl["casrn"])]
    # ids_not_found = [item for item in casrn if item not in dat_cl["casrn"].values]
    # ids_found = casrn_array[np.isin(casrn_array, dat_cl["casrn"])]
    
    out = dat_cl.copy()
    out["query"] = out["casrn"]

    if len(ids_not_found) > 0:
        dat_not_found = pd.DataFrame(columns=col_names)
        dat_not_found["query"] = ids_not_found
        out = pd.concat([out, dat_not_found], axis=0, ignore_index=True)
        if verbose:
            print(f"CASRN {ids_not_found} not found.")

    return out
