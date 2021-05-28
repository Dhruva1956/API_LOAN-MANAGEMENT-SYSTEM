import utils, db
from constants import loanInv, DocumentType, collectionName, misc_webargs, loanCust, roles
import pymongo

def generateUsersUniqueIndex():
    expr = [(misc_webargs.USERNAME.name, pymongo.TEXT)]
    uniqueKey = True
    return db.create_index(collectionName.users.name, expr, uniqueKey)

def insertInitialCounterValue():
    db.insert_one_doc(collectionName.counters.name,{"_id": loanCust.LOAN_CUST_ID.name, misc_webargs.SEQ_VAL.name: 0})

def generateLoan1():
    loanTypeDoc = {
        loanInv.ID.name: "1",
        loanInv.NAME.name: "RedCarpetUp Loan's",
        loanInv.DESC.name: "RedCarpetUp Loan's premium loan service is designed by our bank for private sector individuals wanting quick loans without much hassle.",
        loanInv.MIN_AMT.name: 30000,           
        loanInv.MAX_AMT.name: 3000000,  
        loanInv.MIN_DURATION.name: 12,    
        loanInv.MAX_DURATION.name: 60,    
        loanInv.INTERESTRATE.name: 6,
        loanInv.MANDATORY_REQUIREMENT1.name:DocumentType.PAN_CARD.name,
        loanInv.MANDATORY_REQUIREMENT2.name:DocumentType.SALARY_SLIP.name,
        loanInv.EMI_AVAILABLE.name: True,
        loanInv.PREPAYMENT_AVAILABLE.name: True,
        loanInv.PREPAYMENT_CHARGES.name: 0,
        loanInv.LOAN_PROCESSING_CHARGES.name: 5,
        loanInv.EXTRA_ONE_TIME_CHARGES.name: 500,
        loanInv.MINIMUM_CREDIT_SCORE.name: 700,
        loanInv.MINIMUM_ANNUAL_INCOME_LOANEE.name: 200000,
        loanInv.MINIMUM_MONTHLY_INCOME_LOANEE.name: 10000,
        loanInv.IS_REDUCING_RATE_OF_INTEREST.name: True,
        misc_webargs.TIMESTAMP.name:utils.generate_current_utc()
    }
    return db.insert_one_doc(collectionName.loan_inventory.name,loanTypeDoc)

def generateLoanInventoryIndex():
    expr = [('ID',pymongo.ASCENDING)]
    uniqueKey = True
    return db.create_index(collectionName.loan_inventory.name,expr,uniqueKey)

def generateSuperadmin():
    superadmindoc = {
        misc_webargs.USERNAME.name: "mainadmin",
        misc_webargs.PASSWORD.name: utils.generate_hashedPassword("lee2AURA@@"),
        misc_webargs.ROLE.name: roles.ADMIN.name,
        misc_webargs.TIMEZONE.name: "Asia/Kolkata",
        misc_webargs.TIMESTAMP.name: utils.generate_current_utc()
    }
    return db.insert_one_doc(collectionName.users.name,superadmindoc)