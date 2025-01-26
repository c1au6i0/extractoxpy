import pytest
import extractoxpy as extr
import pandas as pd
import warnings
import time 

ids_search = "bella"
out = extr.extr_ice(casrn = ids_search, verbose = False)

# def test_extr_ice_fetches_data(capsys):
#     ids_search = ["50-00-0", "1332-21-4", "bella", "ciao"]
#     col_names = [
#         "assay", "endpoint", "substance_type", "casrn", "qsar_ready_id",
#         "value", "unit", "species", "receptor_species", "route", "sex",
#         "strain", "life_stage", "tissue", "lesion", "location",
#         "assay_source", "in_vitro_assay_format", "reference",
#         "reference_url", "dtxsid", "substance_name", "pubmed_id", "query"
#     ]

#     out = extr.extr_ice(casrn=ids_search, verbose = True)  # Call the function

#     # Capture printed output
#     captured = capsys.readouterr()
#     assert len(captured.out.strip()) > 0  # Ensure something was printed

#     # Assertions
#     assert isinstance(out, pd.DataFrame)  # Ensure the output is a DataFrame
#     assert list(out.columns) == col_names  # Check the DataFrame columns
#     assert out.shape[0] == 287  # Check the number of rows in the DataFrame
#     assert all(item in out['query'].values for item in ["bella", "ciao"])  # Check query values



# # time.sleep(3)

# # def test_extr_ice_fetches_1_casrn(capsys): 
    
# #     ids_search = "bella"
# #     out = extr.extr_ice(casrn = ids_search, verbose = False)


# #     captured = capsys.readouterr()
    
# #     assert len(captured.out.strip()) == 0

# #   expect_equal(sum(is.na(out$casrn)), 1)
# #   expect_true(is.data.frame(out))
# #   expect_equal(names(out), col_names)
# #   expect_equal(nrow(out), 1)
# # })

# # test_that("extr_ice generate results with 2 casrn", {
# #   skip_on_cran()
# #   skip_if_offline()

# #   ids_search <- c("bella", "ciao")

# #   expect_no_warning({
# #     out <- extr_ice(casrn = ids_search, verbose = FALSE)
# #   })

# #   expect_equal(sum(is.na(out$casrn)), 2)
# #   expect_true(is.data.frame(out))
# #   expect_equal(names(out), col_names)
# #   expect_equal(nrow(out), 2)
# # })

# # # @@@@@@@@@@@@@@@@@@@@@@
# # # TEST FIND ASSAYS. ---
# # # @@@@@@@@@@@@@@@@@@@@@@

# # test_that("extr_ice_assay_names returns 2030 elements with NULL", {
# #   result <- extr_ice_assay_names()
# #   expect_equal(length(result), 2030)
# # })

# # # Test 2: When searching for "opera", it should return exactly 45 elements
# # test_that("extr_ice_assay_names returns 45 elements for 'opera' search", {
# #   result <- extr_ice_assay_names("OPERA")
# #   expect_equal(length(result), 45) #
# # })

# # test_that("extr_ice_assay_names returns 0 elements for '10' search", {
# #   expect_error(extr_ice_assay_names(10))
# # })
