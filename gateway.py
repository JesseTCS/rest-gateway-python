import json
import requests
from sys import version_info
if (version_info > (3, 0)):
     # Import urljoin for Python 3
     from urllib.parse import urljoin
else:
     # Import urljoin for Python 2
     from urlparse import urljoin


global version

class Blaze:
    """ Author: Patrick Petrino | Last Revision: 6/15/2015 | Version: 1.0.0 | This class is required for all Python code making a call to 1stPayBlaze. Please refer to the gateway documentation web page for specifics on what parameters to use for each call."""
    def __init__(self, transactionData):
        self.version = "1.0.0"
        self.apiUrl = "https://secure.1stpaygateway.net/secure/1stPayClientProxy/Gateway/Transaction/"
        self.data={}
        for key in transactionData:
            i = key
            self.data[i] = transactionData[i]
        self.status=str()
        self.result={}
        #raw_response variable used for troubleshooting, should not be needed in normal use.
        self.raw_response={}
        self.responsecode=""
        return
    
    def performRequest(self):
        # Set self.status and self.result to empty so that it can store the new request
        self.status = str()
        self.result = {}
        self.responsedata = ""
        url = self.apiRequest
        postdata = dict(self.data)
        results = requests.post(url,data=postdata)
        response = json.loads(results.text)
        self.responsecode = str(results.status_code)
        self.raw_response = dict(response)
        if response['isError'] == True:
            self.status = 'Error'
            self.result['isError'] = response['isError']
            self.result['errors'] = response['errorMessages']
            self.result['isValid'] = False
            self.result['validations'] = response['validationFailures']
            return self.result
        elif response['validationHasFailed'] == True:
            self.status = 'Validation'
            self.result['isError'] = response['isError']
            self.result['errors'] = response['errorMessages']
            self.result['isValid'] = False
            self.result['validations'] = response['validationFailures']
            return self.result
        elif response['isSuccess'] == True:
            self.status = 'Success'
            if (isinstance(response['data'], dict)) and ('isPartial' in response['data'].keys()) and(response['data']['isPartial'] == True):
                 #To pull partial response must 1) check if the response data is in fact a dictionary, 2) if 'isPartial' is present, and 3) if it is True.
                 #Due to some of the more irregular responses from 1stpayblaze methods (i.e. getAchCategories) there is no other way to do this.
                 self.result['partialOrder'] = dict()
                 self.result['partialOrder']['partialId'] = response['data']['partialId']
                 self.result['partialOrder']['amountRemaining'] = (response['data']['originalFullAmount'] - response['data']['partialAmountApproved'])
                 self.result['partialOrder']['originalFullAmount'] = response['data']['originalFullAmount']
                 self.result['partialOrder']['amountApproved'] = response['data']['partialAmountApproved']
                 self.result['orderId'] = response['data']['orderId']
                 self.result['authCode'] = response['data']['authCode']
                 return self.result
            else:
                 #self.result['data'] = response['data']
                 self.result = response['data']
                 return self.result
        else:
            return("Did not receive proper response. Check input and try again.")
        
    
    def createAuth(self):
        self.apiRequest = urljoin(self.apiUrl,"Auth")
        return(Blaze.performRequest(self))
    
    def createAuthUsing1stPayVault(self):
        self.apiRequest = urljoin(self.apiUrl,"AuthUsingVault")
        return(Blaze.performRequest(self))
    
    def createSale(self):
        self.apiRequest = urljoin(self.apiUrl,"Sale")
        return(Blaze.performRequest(self))
        
    def createSaleUsing1stPayVault(self):
        self.apiRequest = urljoin(self.apiUrl,"SaleUsingVault")
        return(Blaze.performRequest(self))
    
    def createCredit(self):
        self.apiRequest = urljoin(self.apiUrl,"Credit")
        return(Blaze.performRequest(self))
    
    def createCreditRetailOnly(self):
        self.apiRequest = urljoin(self.apiUrl,"CreditRetailOnly")
        return(Blaze.performRequest(self))
    
    def createCreditRetailOnlyUsing1stPayVault(self):
        self.apiRequest = urljoin(self.apiUrl,"CreditRetailOnlyUsingVault")
        return(Blaze.performRequest(self))
    
    def performVoid(self):
        self.apiRequest = urljoin(self.apiUrl,"Void")
        return(Blaze.performRequest(self))

    # The partial void function is not currently used. Specify transactionAmount when running void instead.  
    def performPartialVoid(self):
        self.apiRequest = urljoin(self.apiUrl,"VoidPartial")
        return(Blaze.performRequest(self))
    
    def createReAuth(self):
        self.apiRequest = urljoin(self.apiUrl,"ReAuth")
        return(Blaze.performRequest(self))
    
    def createReSale(self):
        self.apiRequest = urljoin(self.apiUrl,"ReSale")
        return(Blaze.performRequest(self))
    
    def createReDebit(self):
        self.apiRequest = urljoin(self.apiUrl,"ReDebit")
        return(Blaze.performRequest(self))
    
    def query(self):
        self.apiRequest = urljoin(self.apiUrl,"Query")
        return(Blaze.performRequest(self))
    
    def closeBatch(self):
        self.apiRequest = urljoin(self.apiUrl,"CloseBatch")
        return(Blaze.performRequest(self))

    def performSettle(self):
        self.apiRequest = urljoin(self.apiUrl,"Settle")
        return(Blaze.performRequest(self))
    
    def applyTipAdjust(self):
        self.apiRequest = urljoin(self.apiUrl,"TipAdjust")
        return(Blaze.performRequest(self))
    
    def performAchVoid(self):
        self.apiRequest = urljoin(self.apiUrl,"AchVoid")
        return(Blaze.performRequest(self))
    
    def createAchCredit(self):
        self.apiRequest = urljoin(self.apiUrl,"AchCredit")
        return(Blaze.performRequest(self))
    
    def createAchDebit(self):
        self.apiRequest = urljoin(self.apiUrl,"AchDebit")
        return(Blaze.performRequest(self))
    
    def createAchCreditUsing1stPayVault(self):
        self.apiRequest = urljoin(self.apiUrl,"AchCreditUsingVault")
        return(Blaze.performRequest(self))
    
    def createAchDebitUsing1stPayVault(self):
        self.apiRequest = urljoin(self.apiUrl,"AchDebitUsingVault")
        return(Blaze.performRequest(self))
    
    def getAchCategories(self):
        self.apiRequest = urljoin(self.apiUrl,"AchGetCategories")
        return(Blaze.performRequest(self))
		
    def createAchCategories(self):
         self.apiRequest = urljoin(self.apiUrl,"AchCreateCategory")
         return(Blaze.performRequest(self))

    def deleteAchCategories(self):
         self.apiRequest = urljoin(self.apiUrl,"AchDeleteCategory")
         return(Blaze.performRequest(self))

    def setupAchStore(self):
         self.apiRequest = urljoin(self.apiUrl,"AchSetupStore")
         return(Blaze.performRequest(self))
    
    def createVaultContainer(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultCreateContainer")
        return(Blaze.performRequest(self))
    
    def createVaultAchRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultCreateAchRecord")
        return(Blaze.performRequest(self))
    
    def createVaultCreditCardRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultCreateCCRecord")
        return(Blaze.performRequest(self))

    def createVaultShippingRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultCreateShippingRecord")
        return(Blaze.performRequest(self))
    
    def deleteVaultContainerAndAllAsscData(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultDeleteContainerAndAllAsscData")
        return(Blaze.performRequest(self))
    
    def deleteVaultAchRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultDeleteAchRecord")
        return(Blaze.performRequest(self))
    
    def deleteVaultCreditCardRecord(self):       
        self.apiRequest = urljoin(self.apiUrl,"VaultDeleteCCRecord")
        return(Blaze.performRequest(self))
    
    def deleteVaultShippingRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultDeleteShippingRecord")
        return(Blaze.performRequest(self))
    
    def updateVaultContainer(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultUpdateContainer")
        return(Blaze.performRequest(self))
    
    def updateVaultAchRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultUpdateAchRecord")
        return(Blaze.performRequest(self))
    
    def updateVaultCreditCardRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultUpdateCCRecord")
        return(Blaze.performRequest(self))
    
    def updateVaultShippingRecord(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultUpdateShippingRecord")
        return(Blaze.performRequest(self))
    
    def queryVaults(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultQueryVault")
        return(Blaze.performRequest(self))
    
    def queryVaultForCreditCardRecords(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultQueryCCRecord")
        return(Blaze.performRequest(self))
    
    def queryVaultForAchRecords(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultQueryAchRecord")
        return(Blaze.performRequest(self))
    
    def queryVaultForShippingRecords(self):
        self.apiRequest = urljoin(self.apiUrl,"VaultQueryShippingRecord")
        return(Blaze.performRequest(self))
    
    def generateTokenFromCreditCard(self):
        self.apiRequest = urljoin(self.apiUrl,"GenerateTokenFromCreditCard")
        return(Blaze.performRequest(self))
    
    def getCreditCardFromToken(self):
        self.apiRequest = urljoin(self.apiUrl,"GetCreditCardFromToken")
        return(Blaze.performRequest(self))
