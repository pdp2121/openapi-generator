# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.submit_success_response_v1 import SubmitSuccessResponseV1

class TestSubmitSuccessResponseV1(unittest.TestCase):
    """SubmitSuccessResponseV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubmitSuccessResponseV1:
        """Test SubmitSuccessResponseV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubmitSuccessResponseV1`
        """
        model = SubmitSuccessResponseV1()
        if include_optional:
            return SubmitSuccessResponseV1(
                tx_json = None,
                forwarded = True,
                status = 'success',
                warning = '',
                warnings = [
                    openapi_client.models.response_warning.ResponseWarning(
                        details = {
                            'key' : ''
                            }, 
                        id = 56, 
                        message = '', )
                    ],
                engine_result = '',
                engine_result_code = 56,
                engine_result_message = '',
                tx_blob = '',
                accepted = True,
                account_sequence_available = 1.337,
                account_sequence_next = 1.337,
                applied = True,
                broadcast = True,
                kept = True,
                queued = True,
                open_ledger_cost = '',
                validated_ledger_index = 56
            )
        else:
            return SubmitSuccessResponseV1(
                status = 'success',
        )
        """

    def testSubmitSuccessResponseV1(self):
        """Test SubmitSuccessResponseV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
