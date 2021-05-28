from flask import Flask,jsonify
from flask_restful import Api
from webargs.flaskparser import parser,abort
import routes
import db, constants, utils, initial_setup

app = Flask(__name__)
db.init_app(app)
api = Api(app)

@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_headers):
    abort(error_status_code, errors=err.messages)


api.add_resource(routes.Setup,'/setup')
api.add_resource(routes.UserList,'/userList')
api.add_resource(routes.UserEdit,'/userEdit')
api.add_resource(routes.LoansList, '/loansList')
api.add_resource(routes.LoanRequest,'/loanRequest')
api.add_resource(routes.ViewLoan,'/viewLoan')
api.add_resource(routes.EditLoan,'/editLoan')
api.add_resource(routes.ApproveLoan,'/approveLoan')
api.add_resource(routes.UserLogin,'/userLogin')
api.add_resource(routes.UserRegistration, '/userRegistration')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)