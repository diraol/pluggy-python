# AutomaticPixPaymentErrorDetail

Details about an error that occurred with the automatic PIX payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error codes expected during payment processing: - SALDO_INSUFICIENTE: The selected account does not have sufficient balance to make the payment. - VALOR_ACIMA_LIMITE: Validates if the amount exceeds the limit established [by the institution (account or channel)/in the arrangement] to allow the client to perform transactions. - VALOR_INVALIDO: The submitted amount is not valid. - NAO_INFORMADO: Not reported/identified by the account-holding institution. - PAGAMENTO_DIVERGENTE_CONSENTIMENTO: Payment data differs from consent data. - PAGAMENTO_RECUSADO_DETENTORA: [description of the reason for refusal]. - PAGAMENTO_RECUSADO_SPI: [error code according to PACS.002 reason domain table]. - CONSENTIMENTO_INVALIDO: Invalid consent (in final status). - FALHA_INFRAESTRUTURA_SPI: Indicates a failure in the Instant Payments System (SPI). - FALHA_INFRAESTRUTURA_ICP: Indicates a failure in the Public Key Infrastructure (ICP). - FALHA_INFRAESTRUTURA_PSP_RECEBEDOR: Indicates a failure in the infrastructure of the Payment Service Provider (PSP) that receives the payment. - FALHA_INFRAESTRUTURA_DETENTORA: Indicates a failure in the infrastructure of the institution holding the information or resources. - TITULARIDADE_INCONSISTENTE: Account currently not associated with the CPF/CNPJ of the long-term consent. - LIMITE_PERIODO_VALOR_EXCEDIDO: The transaction cannot be performed because the amount parameterized in the consent has been exceeded. - LIMITE_PERIODO_QUANTIDADE_EXCEDIDO: The transaction cannot be performed because the quantity parameterized in the consent has been exceeded. - LIMITE_VALOR_TOTAL_CONSENTIMENTO_EXCEDIDO: The transaction amount exceeds the global consent limit. - LIMITE_VALOR_TRANSACAO_CONSENTIMENTO_EXCEDIDO: The transaction amount exceeds the per-transaction limit set in the consent. - LIMITE_TENTATIVAS_EXCEDIDO: The maximum number of settlement attempts allowed by the arrangement has been reached. - CONSENTIMENTO_REVOGADO: The payment was associated with a consent that has been revoked. - FORA_PRAZO_PERMITIDO: The request time or period does not allow scheduling by the holder. - DETALHE_TENTATIVA_INVALIDO: The parameter(s) [field_name(s)] entered for the new payment attempt do not match the original failed payment and are not allowed in the new attempt. - DETALHE_PAGAMENTO_INVALIDO: Validates if a given parameter provided complies with the business rules. | 
**detail** | **str** | Additional details about the error | 

## Example

```python
from pluggy_sdk.models.automatic_pix_payment_error_detail import AutomaticPixPaymentErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AutomaticPixPaymentErrorDetail from a JSON string
automatic_pix_payment_error_detail_instance = AutomaticPixPaymentErrorDetail.from_json(json)
# print the JSON string representation of the object
print(AutomaticPixPaymentErrorDetail.to_json())

# convert the object into a dict
automatic_pix_payment_error_detail_dict = automatic_pix_payment_error_detail_instance.to_dict()
# create an instance of AutomaticPixPaymentErrorDetail from a dict
automatic_pix_payment_error_detail_from_dict = AutomaticPixPaymentErrorDetail.from_dict(automatic_pix_payment_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


