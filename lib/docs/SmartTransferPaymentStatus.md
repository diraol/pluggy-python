# SmartTransferPaymentStatus

Lifecycle of a Smart Transfer payment. Narrower than `PaymentIntentStatus`: Smart Transfer payments operate under an already-authorized preauthorization, so consent-collection statuses (`STARTED`, `ENQUEUED`, `CONSENT_AWAITING_AUTHORIZATION`) and consent-revocation statuses (`REJECTED`, `REVOKED`, `CONSUMED`) do not apply. - `CONSENT_AUTHORIZED`: the payment was accepted under the preauthorization and is ready to be processed. - `CONSENT_REJECTED`: the preauthorization was rejected at execution time. - `PAYMENT_PENDING`: the payment was submitted to the institution and is awaiting confirmation. - `PAYMENT_PARTIALLY_ACCEPTED`: the payment was accepted but still needs an additional authorization. - `PAYMENT_SETTLEMENT_PROCESSING`: the settlement is being processed. - `PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT`: the funds were debited from the payer account; awaiting clearing. - `PAYMENT_COMPLETED`: the payment was confirmed by the institution. - `PAYMENT_REJECTED`: the payment was rejected after consent was authorized. - `ERROR`: an unexpected error occurred during the flow. - `CANCELED`: the payment was canceled.

## Enum

* `CONSENT_AUTHORIZED` (value: `'CONSENT_AUTHORIZED'`)

* `CONSENT_REJECTED` (value: `'CONSENT_REJECTED'`)

* `PAYMENT_PENDING` (value: `'PAYMENT_PENDING'`)

* `PAYMENT_PARTIALLY_ACCEPTED` (value: `'PAYMENT_PARTIALLY_ACCEPTED'`)

* `PAYMENT_SETTLEMENT_PROCESSING` (value: `'PAYMENT_SETTLEMENT_PROCESSING'`)

* `PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT` (value: `'PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT'`)

* `PAYMENT_COMPLETED` (value: `'PAYMENT_COMPLETED'`)

* `PAYMENT_REJECTED` (value: `'PAYMENT_REJECTED'`)

* `ERROR` (value: `'ERROR'`)

* `CANCELED` (value: `'CANCELED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


