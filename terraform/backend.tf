terraform {

  backend "azurerm" {

    resource_group_name  = "berosetto"

    storage_account_name = "backendberosetto"

    container_name       = "tfstate"
    
    key                  = "terraform.tfstate"

  }

}