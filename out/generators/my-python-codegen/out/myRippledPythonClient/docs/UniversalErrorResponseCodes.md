# UniversalErrorResponseCodes

* `amendmentBlocked` - The server is amendment blocked and needs to be updated to the latest version to stay synced with the XRP Ledger network. * `failedToForward` - (Reporting Mode servers only) The server tried to forward this request to a P2P Mode server, but the connection failed. * `invalid_API_version` - The server does not support the API version number from the request. * `noClosed` - The server does not have a closed ledger, typically because it has not finished starting up. * `noCurrent` - The server does not know what the current ledger is, due to high load, network problems, validator failures, incorrect configuration, or some other problem. * `noNetwork` - The server is having trouble connecting to the rest of the XRP Ledger peer-to-peer network (and is not running in stand-alone mode). * `tooBusy` - The server is under too much load to do this command right now. Generally not returned if you are connected as an admin. * `unknownCmd` - The request does not contain a command that the rippled server recognizes. 

## Enum

* `AMENDMENTBLOCKED` (value: `'amendmentBlocked'`)

* `FAILEDTOFORWARD` (value: `'failedToForward'`)

* `INVALID_API_VERSION` (value: `'invalid_API_version'`)

* `NOCLOSED` (value: `'noClosed'`)

* `NOCURRENT` (value: `'noCurrent'`)

* `NONETWORK` (value: `'noNetwork'`)

* `TOOBUSY` (value: `'tooBusy'`)

* `UNKNOWNCMD` (value: `'unknownCmd'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


