# PaymentIntentStatus

Lifecycle of a payment intent. The flow goes from consent collection (CONSENT_*) to payment execution (PAYMENT_*).  **Consent phase** - `STARTED`: the consent process started at Pluggy. - `ENQUEUED`: the payment is enqueued waiting for the consent flow to be initiated. - `CONSENT_AWAITING_AUTHORIZATION`: the payer must complete the authorization at the institution (see `consentUrl`). - `CONSENT_AUTHORIZED`: the consent was granted by the payer. - `CONSENT_REJECTED`: the consent was rejected by the payer or the institution.  **Payment phase** - `PAYMENT_PENDING`: the payment was submitted to the institution and is waiting confirmation. - `PAYMENT_PARTIALLY_ACCEPTED`: the payment was accepted but still needs an additional authorization (e.g. multi-signature accounts). - `PAYMENT_SETTLEMENT_PROCESSING`: the settlement is being processed. - `PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT`: the funds were debited from the payer account; awaiting clearing. - `PAYMENT_COMPLETED`: the payment was confirmed by the institution. - `PAYMENT_REJECTED`: the payment was rejected after consent was authorized.  **Terminal / other** - `REJECTED`: generic rejected status (institution-specific reason in `errorDetail`). - `ERROR`: an unexpected error occurred during the flow. - `CANCELED`: the intent was canceled. - `REVOKED`: the consent was revoked after authorization (recurring payments only). - `CONSUMED`: the consent was fully consumed (recurring payments reached their end).

## Enum

* `STARTED` (value: `'STARTED'`)

* `ENQUEUED` (value: `'ENQUEUED'`)

* `CONSENT_AWAITING_AUTHORIZATION` (value: `'CONSENT_AWAITING_AUTHORIZATION'`)

* `CONSENT_AUTHORIZED` (value: `'CONSENT_AUTHORIZED'`)

* `CONSENT_REJECTED` (value: `'CONSENT_REJECTED'`)

* `PAYMENT_PENDING` (value: `'PAYMENT_PENDING'`)

* `PAYMENT_PARTIALLY_ACCEPTED` (value: `'PAYMENT_PARTIALLY_ACCEPTED'`)

* `PAYMENT_SETTLEMENT_PROCESSING` (value: `'PAYMENT_SETTLEMENT_PROCESSING'`)

* `PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT` (value: `'PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT'`)

* `PAYMENT_COMPLETED` (value: `'PAYMENT_COMPLETED'`)

* `PAYMENT_REJECTED` (value: `'PAYMENT_REJECTED'`)

* `REJECTED` (value: `'REJECTED'`)

* `ERROR` (value: `'ERROR'`)

* `CANCELED` (value: `'CANCELED'`)

* `REVOKED` (value: `'REVOKED'`)

* `CONSUMED` (value: `'CONSUMED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


