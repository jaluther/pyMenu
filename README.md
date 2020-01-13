# pyMenu
Simple SSH menu using python and YAML data model

##Usage
###User id

When launching the menu you'll be asked to enter your user id.  This will be used to connect to all SSH devices.

However if you want to override the default user id for a specific connection then define userid after selecting a menu item.  For example to launch a connection to a menu item 1 type "1", to connect to menu item 1 with user root type "1 root"

###Search
Within the search menu you can search for the following
·         hostname (partial match)
·         vendor (exact match)
·         model (exact match)


##Maintenance

###Querying the Inventory

The SSH menu is driven by the contents of the "inventory.yml" file in the same directory as the "menu" python script.

To get a list of vendor and model codes used in the Inventory file, then use the following Linux commands:

less inventory.yml | grep vendor | sort -u
less inventory.yml | grep model | sort -u


Whilst building the inventory each device is categorised by vendor and model based on regexp matching of the SNMP sysDescription data.  Categorised devices will have a key/value pair created for both vendor and model. Any devices that have not been categorised will instead have a key/value pair for sysDescription.

To get a count of how many devices have been categorised:
less inventory.yml | grep model | wc -l

To get a count of how many devices have not been categorised:
less inventory.yml | grep sysDescription | wc -l


