# PaymentIntentErrorDetail

Details about an error that occurred with the payment intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error codes expected during payment intent processing: - TEMPO_EXPIRADO_AUTORIZACAO: Consent expired. - CONNECTION_ERROR: Connection error with the institution. - VALOR_ACIMA_LIMITE: Amount exceeds the limit established by the institution or arrangement to allow the client to perform transactions. - FALHA_INFRAESTRUTURA_DETENTORA: Indicates a failure in the infrastructure of the institution holding the information or resources. - FALHA_INFRAESTRUTURA_DETENTORA_CALLBACK_HYBRID_FLOW: Infrastructure failure in the callback hybrid flow. - SALDO_INSUFICIENTE: The selected account does not have sufficient balance to make the payment. - CONTAS_ORIGEM_DESTINO_IGUAIS: Payment failure due to source and destination accounts being the same. - EXPIRED_PAYMENT_INITIATION: Payment initiation expired. - DATA_PAGAMENTO_INVALIDA: Invalid payment date. The scheduled payment end date must be at most 2 years from the start date. - CONSENTIMENTO_PENDENTE_AUTORIZACAO: Consent pending authorization. - TEMPO_EXPIRADO_CONSUMO: Consent expired. - PAYMENT_INTENT_INVALID_CPF: Invalid CPF. - PAYMENT_INTENT_INVALID_CNPJ: Invalid CNPJ. - FALHA_AGENDAMENTO_PAGAMENTOS: Failed to schedule payments. - PAGAMENTO_DIVERGENTE_CONSENTIMENTO: Payment data differs from consent data. - CONTA_NAO_PERMITE_PAGAMENTO: Account does not allow payments. - REJEITADO_USUARIO: Consent canceled by the user. - TIMEOUT_CONSENTIMENTO: Consent timeout. - PAGAMENTO_RECUSADO_SPI: Payment refused by the Instant Payments System (SPI). - REVOGADO_RECEBEDOR: Consent canceled by the receiver. - NAO_INFORMADO: Not reported/identified by the account-holding institution. - AUTENTICACAO_DIVERGENTE: Invalid consent. - TITULARIDADE_INCONSISTENTE: Account currently not associated with the CPF/CNPJ of the long-term consent. - PAGAMENTO_RECUSADO_DETENTORA: Payment refused by the account-holding institution. | 
**provider_code** | **str** | Provider error code | 
**provider_title** | **str** | Provider error title | 
**provider_detail** | **str** | Provider detailed error description | 

## Example

```python
from pluggy_sdk.models.payment_intent_error_detail import PaymentIntentErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentErrorDetail from a JSON string
payment_intent_error_detail_instance = PaymentIntentErrorDetail.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentErrorDetail.to_json())

# convert the object into a dict
payment_intent_error_detail_dict = payment_intent_error_detail_instance.to_dict()
# create an instance of PaymentIntentErrorDetail from a dict
payment_intent_error_detail_from_dict = PaymentIntentErrorDetail.from_dict(payment_intent_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


