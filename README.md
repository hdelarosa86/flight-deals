# Flight Search with SMS Notifications

## Description:

This application is designed to retrieve flight data from Tequila API by 
making specific queries and storing that data in a Google Sheet spreadsheet by
using Sheety API. Using parameters such as length of stay and giving it a range,
we can retrieve the lowest price for a round trip to any city. In this case, I searched
for flights within 180 days from "tomorrow" and a stay of 7 days minimum and up to 28 days.
If there is a cheaper flight than the one currently in the Google Sheet spreadsheet, then
the application sends a Twilio SMS with the new flight information such as price, departure
information, length of stay, and return information.

## Built with...

* Python
* Twilio
* Tequila API
* Sheety
* OOP paradigm

