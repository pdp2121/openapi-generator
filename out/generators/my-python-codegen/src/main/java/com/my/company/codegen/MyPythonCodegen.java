package com.my.company.codegen;

import org.openapitools.codegen.CodegenConfig;
import org.openapitools.codegen.SupportingFile;
import org.openapitools.codegen.languages.PythonClientCodegen;
import org.openapitools.codegen.model.ModelsMap;
import org.openapitools.codegen.model.ModelMap;
import org.openapitools.codegen.CodegenModel;
import org.openapitools.codegen.utils.StringUtils;
import org.openapitools.codegen.utils.CamelizeOption;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyPythonCodegen extends PythonClientCodegen implements CodegenConfig {
  private static final Logger LOGGER = LoggerFactory.getLogger(MyPythonCodegen.class);

  public MyPythonCodegen() {
    super();

    // Change the naming convention for the generated files if needed
    modelTemplateFiles.put("model.mustache", ".py");
    apiTemplateFiles.put("api.mustache", ".py");

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
  public ModelsMap postProcessModels(ModelsMap objs) {
    ModelsMap modelsMap = super.postProcessModels(objs);

    for (ModelMap modelMap : modelsMap.getModels()) {
      CodegenModel model = modelMap.getModel();
      if (model.classname.endsWith("Request")) {
        // Derive the method name from the class name
        String methodName = toSnakeCase(model.classname.replace("Request", ""));
        model.vendorExtensions.put("x-method-name", methodName);
      }
    }

    return modelsMap;
  }

  private String toSnakeCase(String input) {
    return StringUtils.camelize(input, CamelizeOption.LOWERCASE_FIRST_CHAR).replaceAll("([a-z])([A-Z])", "$1_$2")
        .toLowerCase();
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