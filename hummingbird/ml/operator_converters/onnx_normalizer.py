# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import torch
from onnxconverter_common.registration import register_converter

from ._base_operator import BaseOperator
from ._normalizer_implementations import Normalizer


def convert_onnx_normalizer(operator, device=None, extra_config={}):
    """
    Converter for `ai.onnx.ml.Normalizer`

    Args:
        operator: An operator wrapping a `ai.onnx.ml.Normalizer` model
        device: String defining the type of device the converted operator should be run on
        extra_config: Extra configuration used to select the best conversion strategy

    Returns:
        A PyTorch model
    """
    raw_operator = operator.origin.attribute[0].s.lower().decode("UTF-8")  # (ex: b'L1' to 'l1')
    if raw_operator is None or raw_operator == "":
        raise RuntimeError("Error parsing Normalizer, found unexpected None")
    return Normalizer(raw_operator, device)


register_converter("ONNXMLNormalizer", convert_onnx_normalizer)
