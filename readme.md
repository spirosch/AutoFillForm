v0.1 (25/10)
- Support form 1

Dependencies
- Folder containing all client data called 'data_form_1'
  - Each client folder contains a subfolder called 'attachments'
  - Each client folder contains an .xlsx file called 'data.xlsx' (name can be irrelavant)

Flow
- For each user 
  - Parse .xlsx and create the relevant python structure matching the data you need for each step of the form
  - Run the web driver with the data from the python structure

v0.2 (25/11)
TODO
- [ ] Create a parser from the excel to python object
- [ ] Replace hardcoded text with dynamic fields 
- [ ] Provide files from command line
- [ ] Provide files from GUI