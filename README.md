# Switch reboot logs

## Disclaimer

The content provided is for inspiration and educational purposes only, not for production use. It is an example to spark ideas, not optimized for real-world environments. Use it as a starting point, but review and test thoroughly before considering it for live applications.

## Description

The script scope all Meraki Oraganization and Network to check boot events in the event log for the switches and returne the list of events with the reason

## API KEY

An API KEY (API_KEY) must be provided, read only permission are enough

https://developer.cisco.com/meraki/api-v1/authorization/#obtaining-your-meraki-api-key

## API endpoint used

[Get Organizations](https://developer.cisco.com/meraki/api-v1/get-organizations/)

[Get Organization Networks](https://developer.cisco.com/meraki/api-v1/get-organization-networks/)

[Get Network Events](https://developer.cisco.com/meraki/api-v1/get-network-events/)
