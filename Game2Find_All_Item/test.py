item_id = {
    "id": "id",

    "name": "id card",

    "description":
    """You new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?..."""
}
SystemOutput = "a"
Counter = len(items)
if Counter == 1:
	SystemOutput = items["name"]
print (SystemOutput)
pass