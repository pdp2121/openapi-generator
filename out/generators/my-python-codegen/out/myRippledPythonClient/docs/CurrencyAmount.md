# CurrencyAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Arbitrary currency code for the token. Cannot be XRP. | [optional] 
**value** | **str** | Quoted decimal representation of the amount of the token. This can include scientific notation, such as 1.23e11 meaning 123,000,000,000. Both e and E may be used. This can be negative when displaying balances, but negative values are disallowed in other contexts such as specifying how much to send. | [optional] 
**issuer** | **str** | Generally, the account that issues this token. In special cases, this can refer to the account that holds the token instead (for example, in a Clawback transaction). | [optional] 

## Example

```python
from openapi_client.models.currency_amount import CurrencyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyAmount from a JSON string
currency_amount_instance = CurrencyAmount.from_json(json)
# print the JSON string representation of the object
print(CurrencyAmount.to_json())

# convert the object into a dict
currency_amount_dict = currency_amount_instance.to_dict()
# create an instance of CurrencyAmount from a dict
currency_amount_from_dict = CurrencyAmount.from_dict(currency_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


