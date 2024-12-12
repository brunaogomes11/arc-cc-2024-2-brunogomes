#!/usr/bin/env python3
from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(f"Endereço buscado: {address}"
          f"Resultado 1:"
          f"CEP: {location.cep}"
          f"(Latitude, Longitude): {location.latitude}, {location.longitude}")
