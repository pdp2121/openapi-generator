# Custom OpenAPI Generator

## Prerequisites

Java and Maven are required

Homebrew:

```
brew install java
brew install maven
```

## Build the custom generator

- Build all generators

```
mvn clean package
```

- Build custom generator

```
cd out/generators/my-python-codegen
mvn clean package
cd ../../..
```

- Generate output models (change the path to desired yaml specs or output folder if needed)

```
java -cp out/generators/my-python-codegen/target/my-python-codegen-openapi-generator-1.0.0.jar:modules/openapi-generator-cli/target/openapi-generator-cli.jar \
  org.openapitools.codegen.OpenAPIGenerator generate -g my-python-codegen \
  -i ./out/generators/my-python-codegen/simple_pet_api.yaml \
  -o ./out/generators/my-python-codegen/out/myPythonClient
```

## Customize the code generator

The code generator can be customized by either:

- Modify the logic within `out/generators/my-python-codegen/src/main/java/com/my/company/codegen/MyPythonCodegen.java` by using polymorphism.

- Modify the mustache templates within `out/generators/my-python-codegen/src/main/resources/my-python-codegen`

For more instructions please refer to the documentations inside `docs`
