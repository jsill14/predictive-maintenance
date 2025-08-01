# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
assets_at_high_priority_python = dataiku.Dataset("assets_at_high_priority_python")
assets_at_high_priority_python_df = assets_at_high_priority_python.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

data2_df = assets_at_high_priority_python_df # For this sample code, simply copy input to output


# Write recipe outputs
data2 = dataiku.Dataset("data2")
data2.write_with_schema(data2_df)
