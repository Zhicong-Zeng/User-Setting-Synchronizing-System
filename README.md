# User-Setting-Synchronizing-System
This project is a system of synchronization user setting within three data storages.
This project has two main deliverables: The Web Page and the RESTful API.
Users can get the data by web page or API. 
This information is display in web page or sent up as JSON objects through API.

## Install dependencies
pip install

## Database Structure
There  are zero, one, or more  key-value pairs in a JSON object starting from the root 
object.
Curly braces will be used to enclose the item. A comma will be used to separate 
each key-value pair.
The key-value pair's order is unimportant. 

## Sample JSON object
{ 
  "Name":"UserName", 
  "DateandTime":"desaturation", 
  "CompanyPhonenumber":"4256334567", 
  "PersonalPhonenumber":"4256334577", 
  "Timezone":"UTC", 
  "Currency":"USD", 
  "PreferredLanguage":"English", 
  "EmailAddress":"user1@company.com", 
  "Role":"Software Engineer", 
  "Address":"901, 12th st Seattle" 
}  

## Test
Postman Get method to test if we can get all the data from three different storages. 

Postman Post method to test if we can update the data to three different storages. 


## Sample GET call (do we need this?)

## Sample POST call (do we need this?)
