from webargs import fields, validate, ValidationError
import auth
import constants, utils
argsLogin = {

    constants.misc_webargs.USERNAME.name: fields.Str(
        required=True, validate=validate.Length(min=1)
    ),

    constants.misc_webargs.PASSWORD.name: fields.Str(
        required=True, validate=validate.Length(min=8)
    )
}
argsUserRegistration = {
    constants.misc_webargs.USERNAME.name: fields.Str(
        required=True, validate=auth.username_must_not_exist_in_db
    ),
    constants.misc_webargs.PASSWORD.name: fields.Str(
        required=True, validate=validate.Length(min=8)
    ),
    constants.misc_webargs.ROLE.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.REFERRER_TOKEN.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.REFERRER_USERNAME.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.TIMEZONE.name: fields.Str(
        required=True, validate=utils.validate_timezone
    )
}
argsUserList = {
    constants.misc_webargs.USERNAME.name: fields.Str(
        required=True, validate=validate.Length(min=1)
    ),
    constants.misc_webargs.TOKEN.name: fields.Str(
        required=True
    )
}
argsUserEdit = {
    constants.misc_webargs.USERNAME.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.REFERRER_USERNAME.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.REFERRER_TOKEN.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.CREDIT_SCORE.name: fields.Int(

    ),
    constants.misc_webargs.DOCUMENT1_VER_STATUS.name: fields.Bool(

    ),
    constants.misc_webargs.DOCUMENT2_VER_STATUS.name: fields.Bool(

    ),
    constants.misc_webargs.TIMEZONE.name: fields.Str(
        validate=utils.validate_timezone
    )
}
argsLoanRequest = {
    constants.misc_webargs.REFERRER_USERNAME.name: fields.Str(
        required=True, validate=validate.Length(min=1)
    ),
    constants.misc_webargs.REFERRER_TOKEN.name: fields.Str(
        required=True
    ),
    constants.misc_webargs.CUSTOMER_NAME.name: fields.Str(
        required=True
    ),
    constants.loanCust.LOAN_INVT_ID.name: fields.Str(
        required=True
    ),
    constants.loanCust.AMT.name: fields.Int(
        required=True
    ),
    constants.loanCust.DURATION.name: fields.Int(
        required=True
    ),
    constants.loanCust.MANDATORY_REQUIREMENT1_LOC.name: fields.Str(
        required=True
    ),
    constants.loanCust.MANDATORY_REQUIREMENT2_LOC.name: fields.Str(
        required=True
    ),
    constants.loanCust.EMI_CHOSEN.name: fields.Bool(
        required=True
    )

}
argsViewLoan = argsUserList
argsEditLoan = {
    constants.misc_webargs.REFERRER_USERNAME.name: fields.Str(required=True, validate=validate.Length(min=1)),
    constants.misc_webargs.REFERRER_TOKEN.name: fields.Str(required=True),
    constants.misc_webargs.CUSTOMER_NAME.name: fields.Str(required=True),
    constants.loanCust.LOAN_CUST_ID.name: fields.Str(required=True),
    constants.loanCust.AMT.name: fields.Int(),
    constants.loanCust.DURATION.name: fields.Int(),
    constants.loanCust.MANDATORY_REQUIREMENT1_LOC.name: fields.Str(),
    constants.loanCust.MANDATORY_REQUIREMENT2_LOC.name: fields.Str(),
}
argsApproveLoan = {
    constants.misc_webargs.REFERRER_USERNAME.name: fields.Str(
        required=True, validate=validate.Length(min=1)
    ), constants.misc_webargs.REFERRER_TOKEN.name: fields.Str(
        required=True
    ), constants.loanCust.LOAN_CUST_ID.name: fields.Str(
        required=True
    ), constants.loanCust.LOAN_STATE.name: fields.Str(
        required=True, validate=validate.OneOf([constants.loanState.ACCEPTED.name, constants.loanState.REJECTED.name])
    )
}