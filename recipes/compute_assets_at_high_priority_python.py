# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Assets_at_high_priority = dataiku.Dataset("Assets_at_high_priority")
Assets_at_high_priority_df = Assets_at_high_priority.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

assets_at_high_priority_python_df = Assets_at_high_priority_df # For this sample code, simply copy input to output


# Write recipe outputs
assets_at_high_priority_python = dataiku.Dataset("assets_at_high_priority_python")
assets_at_high_priority_python.write_with_schema(assets_at_high_priority_python_df)
