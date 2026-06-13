# PaymentRequestStatus

Lifecycle of a payment request. - `CREATED`: the request was created and is waiting for a payment intent. - `IN_PROGRESS`: a payment intent is being processed by the institution. - `WAITING_PAYER_AUTHORIZATION`: the payer must authorize the payment at the institution. - `AUTHORIZED`: only for Automatic PIX. The recurring consent was authorized; individual payments will be executed under it. - `SCHEDULED`: the payment is scheduled for a future date. - `COMPLETED`: the payment was confirmed by the institution. - `ERROR`: the payment failed (see `errorDetail`). - `REFUND_IN_PROGRESS`: a refund was requested and is being processed. - `REFUNDED`: the refund was completed. - `REFUND_ERROR`: the refund failed. - `EXPIRED`: the request expired without being paid. - `CANCELED`: the request was canceled.

## Enum

* `CREATED` (value: `'CREATED'`)

* `IN_PROGRESS` (value: `'IN_PROGRESS'`)

* `WAITING_PAYER_AUTHORIZATION` (value: `'WAITING_PAYER_AUTHORIZATION'`)

* `AUTHORIZED` (value: `'AUTHORIZED'`)

* `SCHEDULED` (value: `'SCHEDULED'`)

* `COMPLETED` (value: `'COMPLETED'`)

* `ERROR` (value: `'ERROR'`)

* `REFUND_IN_PROGRESS` (value: `'REFUND_IN_PROGRESS'`)

* `REFUNDED` (value: `'REFUNDED'`)

* `REFUND_ERROR` (value: `'REFUND_ERROR'`)

* `EXPIRED` (value: `'EXPIRED'`)

* `CANCELED` (value: `'CANCELED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


