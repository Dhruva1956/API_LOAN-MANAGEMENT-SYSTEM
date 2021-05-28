# API_LOAN-MANAGEMENT-SYSTEM
.I used Postman which is a great tool.I used it to dissect my   project and used it to test an API's functionality.
.Backend is made with Python Flask Framework.
.Webargs are used for argument parsing.
.Flask_restful for routing process.
.Mongodb is used as database.
.Docker is used for deployment. 
.The Python Framework adds salt to the password and hashes it and then store it to database.

#Features:
1. List, view and edit users -  this can only be done by "agent" and "admin" roles
2. Create a loan request on behalf of the user -  This can only be done by "agent" role. Inputs would be tenure selected (in months) and interest to be charged every month. Loan can have 3 states - "NEW", "REJECTED", "APPROVED".
3. Approval of loan request - This can only be done by an "admin" role.
4. Edit a loan (but not after it has been approved) -  This can be done only by "agent" role. But cannot be done if loan is in "Approved" state.
5. Ability to list and view loans (approved) or loan requests based on the filter applied. "customer" can only see his own loans...while "agent" and "admin" can see everyone's loans. 

#To run this put a post request at "localhost:5000/setup". It will create a superadmin for testing and also create a loan object in db.
