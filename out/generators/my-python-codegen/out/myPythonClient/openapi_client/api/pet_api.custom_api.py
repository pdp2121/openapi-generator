
# This is a sample api mustache template.  It is representing a fictitious
# language and won't be usable or compile to anything without lots of changes.
# Use it as an example.  You can access the variables in the generator object
# like such:

# use the package from the `apiPackage` variable
package: openapi_client.api

# operations block
classname: PetApi

# loop over each operation in the API:

# each operation has an `operationId`:
operationId: get_pet_by_id

# and parameters:
pet_id: int


# each operation has an `operationId`:
operationId: list_pets

# and parameters:


# end of operations block
