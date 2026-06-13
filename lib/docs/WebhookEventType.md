# WebhookEventType

Event the webhook subscribes to. Use `all` to receive every event for the client. Events are grouped by topic:  **item/** – Lifecycle of an item (a connection to a financial institution). - `item/created`: a new item was created. - `item/updated`: the item finished an execution with new data. - `item/error`: the execution finished with an error (see the payload's `error` field). - `item/deleted`: the item was deleted. - `item/waiting_user_input`: the item needs additional credentials/MFA from the end user. - `item/waiting_user_action`: the item needs the end user to perform an action on the institution side. - `item/login_succeeded`: the credentials were accepted by the institution (data may still be syncing).  **connector/** – Connector-level events. - `connector/status_updated`: a connector's health status changed (ONLINE/OFFLINE/UNSTABLE).  **transactions/** – Account transaction lifecycle. - `transactions/created` / `transactions/updated` / `transactions/deleted`: a transaction was inserted, modified or removed during an item execution.  **payment_intent/** – Payment Initiation flow (single PIX). - `payment_intent/created`: a payment intent was created. - `payment_intent/completed`: the payment was confirmed by the institution. - `payment_intent/waiting_payer_authorization`: the payer still needs to authorize the payment. - `payment_intent/error`: the payment was rejected or failed.  **payment_request/** – Aggregate payment request state. - `payment_request/updated`: the overall status of a payment request changed.  **scheduled_payment/** – Scheduled (recurring or future) payments. - `scheduled_payment/created` / `completed` / `error` / `canceled`: lifecycle of a single scheduled payment. - `scheduled_payment/all_created` / `scheduled_payment/all_completed`: emitted once when every scheduled payment in a series reaches the same terminal state.  **boleto/** – Boleto status updates. - `boleto/updated`: the boleto data was updated (e.g. paid, expired, amount changed).  **automatic_pix_payment/** – Recurring PIX (PIX Automático) individual payments. - `automatic_pix_payment/created`: a new recurring payment was scheduled. - `automatic_pix_payment/completed`: the recurring payment was confirmed. - `automatic_pix_payment/error`: the recurring payment failed. - `automatic_pix_payment/canceled`: the recurring payment was canceled (by user, expiration or revoked consent).  **smart_transfer_preauthorization/** – Smart Transfer pre-authorization (consent setup). - `smart_transfer_preauthorization/completed`: the pre-authorization was accepted. - `smart_transfer_preauthorization/error`: the pre-authorization failed.  **smart_transfer_payment/** – Smart Transfer individual payments executed under an active pre-authorization. - `smart_transfer_payment/completed`: the transfer was successful. - `smart_transfer_payment/error`: the transfer failed.

## Enum

* `ALL` (value: `'all'`)

* `ITEM_SLASH_CREATED` (value: `'item/created'`)

* `ITEM_SLASH_UPDATED` (value: `'item/updated'`)

* `ITEM_SLASH_ERROR` (value: `'item/error'`)

* `ITEM_SLASH_DELETED` (value: `'item/deleted'`)

* `ITEM_SLASH_WAITING_USER_INPUT` (value: `'item/waiting_user_input'`)

* `ITEM_SLASH_WAITING_USER_ACTION` (value: `'item/waiting_user_action'`)

* `ITEM_SLASH_LOGIN_SUCCEEDED` (value: `'item/login_succeeded'`)

* `CONNECTOR_SLASH_STATUS_UPDATED` (value: `'connector/status_updated'`)

* `TRANSACTIONS_SLASH_CREATED` (value: `'transactions/created'`)

* `TRANSACTIONS_SLASH_UPDATED` (value: `'transactions/updated'`)

* `TRANSACTIONS_SLASH_DELETED` (value: `'transactions/deleted'`)

* `PAYMENT_INTENT_SLASH_CREATED` (value: `'payment_intent/created'`)

* `PAYMENT_INTENT_SLASH_COMPLETED` (value: `'payment_intent/completed'`)

* `PAYMENT_INTENT_SLASH_WAITING_PAYER_AUTHORIZATION` (value: `'payment_intent/waiting_payer_authorization'`)

* `PAYMENT_INTENT_SLASH_ERROR` (value: `'payment_intent/error'`)

* `PAYMENT_REQUEST_SLASH_UPDATED` (value: `'payment_request/updated'`)

* `SCHEDULED_PAYMENT_SLASH_CREATED` (value: `'scheduled_payment/created'`)

* `SCHEDULED_PAYMENT_SLASH_COMPLETED` (value: `'scheduled_payment/completed'`)

* `SCHEDULED_PAYMENT_SLASH_ERROR` (value: `'scheduled_payment/error'`)

* `SCHEDULED_PAYMENT_SLASH_CANCELED` (value: `'scheduled_payment/canceled'`)

* `SCHEDULED_PAYMENT_SLASH_ALL_COMPLETED` (value: `'scheduled_payment/all_completed'`)

* `SCHEDULED_PAYMENT_SLASH_ALL_CREATED` (value: `'scheduled_payment/all_created'`)

* `BOLETO_SLASH_UPDATED` (value: `'boleto/updated'`)

* `AUTOMATIC_PIX_PAYMENT_SLASH_CREATED` (value: `'automatic_pix_payment/created'`)

* `AUTOMATIC_PIX_PAYMENT_SLASH_COMPLETED` (value: `'automatic_pix_payment/completed'`)

* `AUTOMATIC_PIX_PAYMENT_SLASH_ERROR` (value: `'automatic_pix_payment/error'`)

* `AUTOMATIC_PIX_PAYMENT_SLASH_CANCELED` (value: `'automatic_pix_payment/canceled'`)

* `SMART_TRANSFER_PREAUTHORIZATION_SLASH_COMPLETED` (value: `'smart_transfer_preauthorization/completed'`)

* `SMART_TRANSFER_PREAUTHORIZATION_SLASH_ERROR` (value: `'smart_transfer_preauthorization/error'`)

* `SMART_TRANSFER_PAYMENT_SLASH_COMPLETED` (value: `'smart_transfer_payment/completed'`)

* `SMART_TRANSFER_PAYMENT_SLASH_ERROR` (value: `'smart_transfer_payment/error'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


