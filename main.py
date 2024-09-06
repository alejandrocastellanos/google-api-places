from google_api_client import GoogleApiPlacesClient

input_text = "AutoMás peritaje calle 134"

instance_google_api_places_client = GoogleApiPlacesClient(name_rtm_headquarters=input_text)
place_details = instance_google_api_places_client.place_details()

print("place_details: ", place_details)

'''
response:
{
    'rating': 4.2, 
    'list_reviews': [
            {'author': 'Denis Tankov', 'text': 'Buenos servicios', 'rating': 5}, 
            {'author': 'Eric Stander', 'text': 'Bueno servicio', 'rating': 5}, 
            {'author': 'Carlos Andres Mariño Leon', 'text': 'Muy rapido la verdad', 'rating': 5}, 
            {'author': 'Gabriel Gomez', 'text': "ningún personal de la sede sabe decirme en qué proceso va mi vehículo", 'rating': 3}, 
            {'author': 'Javier', 'text': 'Servicio realmente rapido', 'rating': 5}
    ], 
    'list_photos': [
        {'reference': 'AXCi2Q5_ISKzzW24xSyDXi-JkU6N9OoMwBegkDWHFoZj9N2mJYsIhrYhBv7blFYp5loFHbaKlMftqOWr2_xGmavmxAAJqwia5vxd_Z3p4zuuvn9GKA4GWSwqTlZVR_9QcSPvQDtjigGpPqMdLwMAOPxPHdCYExGSVFdSOoMSux0-OQXnyjlv', 
        'link': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AXCi2Q5_ISKzzW24xSyDXi-JkU6N9OoMwBegkDWHFoZj9N2mJYsIhrYhBv7blFYp5loFHbaKlMftqOWr2_xGmavmxAAJqwia5vxd_Z3p4zuuvn9GKA4GWSwqTlZVR_9QcSPvQDtjigGpPqMdLwMAOPxPHdCYExGSVFdSOoMSux0-OQXnyjlv'}, 
        {'reference': 'AXCi2Q7XTqmaadFmwzBpOeGYPUYlcaRR_PvLRnAoTWmFXs2BQ0ClFJrad0rEZxlzu3vJ359RNPFcdIWfeE5Z0IuSwr81BTRQfjkrrWlQSr_fqAhxn9AGrHJs3gcQvlfY4XXHDx5GcqvqSJeuWBATD8dNf0FUDkEqGWMAb-bWxZZRwVo4_8BL', 'link': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AXCi2Q7XTqmaadFmwzBpOeGYPUYlcaRR_PvLRnAoTWmFXs2BQ0ClFJrad0rEZxlzu3vJ359RNPFcdIWfeE5Z0IuSwr81BTRQfjkrrWlQSr_fqAhxn9AGrHJs3gcQvlfY4XXHDx5GcqvqSJeuWBATD8dNf0FUDkEqGWMAb-bWxZZRwVo4_8BL&'}, 
        {'reference': 'AXCi2Q4nsXD6gZEddDcNwK4Qz8uvNLISNN7Pp6gseVeQKS3GkCs8m4zO37U5r6uqbugeDYzl2c_6MRzjv1noufPRPeteBI6ZvMltcaESobk71eG08cL7vJYE4CGqY_JuMDUmW6vmKXxXjxVWh4l2PYleIAbqwh91yJ03zCeAF5h8vIgWJ3hF', 'link': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AXCi2Q4nsXD6gZEddDcNwK4Qz8uvNLISNN7Pp6gseVeQKS3GkCs8m4zO37U5r6uqbugeDYzl2c_6MRzjv1noufPRPeteBI6ZvMltcaESobk71eG08cL7vJYE4CGqY_JuMDUmW6vmKXxXjxVWh4l2PYleIAbqwh91yJ03zCeAF5h8vIgWJ3hF&'}
    ]
}
'''
