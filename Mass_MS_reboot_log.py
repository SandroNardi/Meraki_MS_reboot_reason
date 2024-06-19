import os
import meraki
from prettytable import PrettyTable

# API KEY read only permission is enough
API_KEY = os.getenv("MK_TEST_API")

total_pages = 10


dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)


# get all arganization
organizations = dashboard.organizations.getOrganizations()

for org in organizations:
    # get all network
    networks = dashboard.organizations.getOrganizationNetworks(
        org["id"], total_pages="all"
    )

    # for each network if it contains a switch
    for net in networks:
        if "switch" in net["productTypes"]:
            # get network events for the switches in the "boot" category
            events = dashboard.networks.getNetworkEvents(
                net["id"],
                total_pages=total_pages,
                productType="switch",
                includedEventTypes="boot",
            )
            # put in table
            t_devices = PrettyTable(["Time", "Name", "Serial", "Reason"])
            for event in events["events"]:
                t_devices.add_row(
                    [
                        event["occurredAt"],
                        event["deviceName"],
                        event["deviceSerial"],
                        event["eventData"]["reason"],
                    ]
                )
            # print table
            print(t_devices)
