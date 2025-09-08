class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        # if flight_details.status_code == 200:
        #     prices = []
        #     for data in flight_details.json()['data']:
        #         price = data.price.grandTotal
        #         prices.append(price)
        #     return min(prices) if prices else None


def find_cheapest_price(data):
    if data is None:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data[0]
    lowest_price = float(first_flight['price']['grandTotal'])
    origin_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date)

    for flight in data:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            size = len(flight["itineraries"][0]["segments"])
            lowest_price = price
            origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_airport = flight["itineraries"][0]["segments"][size-1]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date)
            print(f"Lowest price to {destination_airport} is ${lowest_price}")

    return cheapest_flight


