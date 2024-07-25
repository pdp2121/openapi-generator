package com.my.company.codegen;

import org.openapitools.codegen.CodegenConfig;
import org.openapitools.codegen.SupportingFile;

public class MyPythonCodegen extends PythonClientCodegen implements CodegenConfig {
  public MyPythonCodegen() {
    super();

    // Change the naming convention for the generated files if needed
    modelTemplateFiles.put("model.mustache", ".custom_model.py");
    apiTemplateFiles.put("api.mustache", ".custom_api.py");

    // Set the template directory
    embeddedTemplateDir = templateDir = "my-python-codegen";
  }

  @Override
  public void processOpts() {
    super.processOpts();

    // Add a custom header to each generated file if needed
    supportingFiles.add(new SupportingFile("custom_header.mustache", "", "custom_header.py"));
  }

  @Override
  public String getName() {
    return "my-python-codegen";
  }

  @Override
  public String getHelp() {
    return "Generates a custom Python client library.";
  }
}