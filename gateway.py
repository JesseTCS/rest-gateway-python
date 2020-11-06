from json import dumps, loads
from requests import post


class RestGateway:
    """
    | Last Revision: 11/06/2020
    | Version: 1.2.1
    | This class is required for all Python code making a call to REST API. Please refer to the gateway documentation web page for specifics on what parameters to use for each call.
    """
    def __init__(self, transactionData):
        self.version = "1.2.1"
        self.apiUrl = "https://secure.1stpaygateway.net/secure/RestGW/Gateway/Transaction/"
        self.TestMode = False
        self.data = {key: transactionData[key] for key in transactionData}
        self.status = self.responsecode = ""
        self.result = {}
        return

    def SwitchEnv(self):
        # Switch between production and validation
        production = "https://secure.1stpaygateway.net/secure/RestGW/Gateway/Transaction/"
        validation = "https://secure-v.goemerchant.com/secure/RestGW/Gateway/Transaction/"
        api_url = self.apiUrl
        url_dict = {production: (validation, True), validation: (production, False)}
        if api_url in url_dict:
            self.apiUrl = url_dict[api_url][0]
            self.TestMode = url_dict[api_url][1]
        else:
            self.apiUrl = production
            self.TestMode = False
        return True

    def _performRequest(self, value):
        # Set self.status and self.result to empty so that it can store the new request
        self.status = self.responsecode = ""
        header = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        url = self.apiUrl + value
        results = post(url, data=dumps(self.data), headers=header)
        response = loads(results.text)
        self.responsecode = str(results.status_code)
        self.result = result = dict(response)
        # Set status according to the appropriate keys, guarding against unexpected return data
        for key, value in {'isSuccess': "Success", 'validationHasFailed': "Validation", 'isError': "Error"}.items():
            if key in result and result[key] is True:
                self.status = value
                break
        else:
            self.status = 'Unknown'
        return result

    def createAuth(self):
        return self._performRequest(value="Auth")

    def createAuthUsing1stPayVault(self):
        return self._performRequest(value="AuthUsingVault")

    def createSale(self):
        return self._performRequest(value="Sale")

    def createSaleUsing1stPayVault(self):
        return self._performRequest(value="SaleUsingVault")

    def createCredit(self):
        return self._performRequest(value="Credit")

    def createCreditRetailOnly(self):
        return self._performRequest(value="CreditRetailOnly")

    def createCreditRetailOnlyUsing1stPayVault(self):
        return self._performRequest(value="CreditRetailOnlyUsingVault")

    def performVoid(self):
        return self._performRequest(value="Void")

    def createReAuth(self):
        return self._performRequest(value="ReAuth")

    def createReSale(self):
        return self._performRequest(value="ReSale")

    def createReDebit(self):
        return self._performRequest(value="ReDebit")

    def query(self):
        return self._performRequest(value="Query")

    def closeBatch(self):
        return self._performRequest(value="CloseBatch")

    def performSettle(self):
        return self._performRequest(value="Settle")

    def applyTipAdjust(self):
        return self._performRequest(value="TipAdjust")

    def performAchVoid(self):
        return self._performRequest(value="AchVoid")

    def createAchCredit(self):
        return self._performRequest(value="AchCredit")

    def createAchDebit(self):
        return self._performRequest(value="AchDebit")

    def createAchCreditUsing1stPayVault(self):
        return self._performRequest(value="AchCreditUsingVault")

    def createAchDebitUsing1stPayVault(self):
        return self._performRequest(value="AchDebitUsingVault")

    def getAchCategories(self):
        return self._performRequest(value="AchGetCategories")

    def createAchCategories(self):
        return self._performRequest(value="AchCreateCategory")

    def deleteAchCategories(self):
        return self._performRequest(value="AchDeleteCategory")

    def setupAchStore(self):
        return self._performRequest(value="AchSetupStore")

    def createVaultContainer(self):
        return self._performRequest(value="VaultCreateContainer")

    def createVaultAchRecord(self):
        return self._performRequest(value="VaultCreateAchRecord")

    def createVaultCreditCardRecord(self):
        return self._performRequest(value="VaultCreateCCRecord")

    def createVaultShippingRecord(self):
        return self._performRequest(value="VaultCreateShippingRecord")

    def deleteVaultContainerAndAllAsscData(self):
        return self._performRequest(value="VaultDeleteContainerAndAllAsscData")

    def deleteVaultAchRecord(self):
        return self._performRequest(value="VaultDeleteAchRecord")

    def deleteVaultCreditCardRecord(self):
        return self._performRequest(value="VaultDeleteCCRecord")

    def deleteVaultShippingRecord(self):
        return self._performRequest(value="VaultDeleteShippingRecord")

    def updateVaultContainer(self):
        return self._performRequest(value="VaultUpdateContainer")

    def updateVaultAchRecord(self):
        return self._performRequest(value="VaultUpdateAchRecord")

    def updateVaultCreditCardRecord(self):
        return self._performRequest(value="VaultUpdateCCRecord")

    def updateVaultShippingRecord(self):
        return self._performRequest(value="VaultUpdateShippingRecord")

    def queryVaults(self):
        return self._performRequest(value="VaultQueryVault")

    def queryVaultForCreditCardRecords(self):
        return self._performRequest(value="VaultQueryCCRecord")

    def queryVaultForAchRecords(self):
        return self._performRequest(value="VaultQueryAchRecord")

    def queryVaultForShippingRecords(self):
        return self._performRequest(value="VaultQueryShippingRecord")

    def modifyRecurring(self):
        return self._performRequest(value="RecurringModify")

    def submitAcctUpdater(self):
        return self._performRequest(value="AccountUpdaterSubmit")

    def submitAcctUpdaterVault(self):
        return self._performRequest(value="AccountUpdaterSubmitVault")

    def getAcctUpdaterReturn(self):
        return self._performRequest(value="AccountUpdaterReturn")

    def generateTokenFromCreditCard(self):
        return self._performRequest(value="GenerateTokenFromCreditCard")