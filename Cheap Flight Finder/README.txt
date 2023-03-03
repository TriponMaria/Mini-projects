1. Pass each city name in sheet_data one-by-one to the FlightSearch class to get the corresponding IATA code for that city using https://api.tequila.kiwi.com/v2/locations/query. I'll update the Google Sheet with the IATA code for each city.

2. I search for the flight prices from London(LON) to all the destinations in the Google Sheet. In this project, I only look for direct flights, that leave anytime between tomorrow and in 6 month time. I also looking for round trips that return between 7 and 28 days in length. (https://api.tequila.kiwi.com/v2/search)

3. I check if any of theflights found are cheaper than the Lowest Price listed in the Google Sheet. If so, than I use the Twilio to send an SMS with enough information to book the flight. I use the NotificationManager for this job.