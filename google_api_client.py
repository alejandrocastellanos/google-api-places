import requests

place_search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
place_details_url = "https://maps.googleapis.com/maps/api/place/details/json"
API_KEY = ''

class GoogleApiPlacesClient:

    def __init__(self, name_rtm_headquarters):
        self._name_rtm_headquarters = name_rtm_headquarters
        self._api_key = API_KEY

    def place_details(self):
        place_id = self._get_place_id()
        if not place_id:
            return {}
        get_place_detail = self._get_place_detail(place_id=place_id)
        return get_place_detail

    def _get_place_id(self):
        _search_params = {
            "input": self._name_rtm_headquarters,
            "inputtype": "textquery",
            "fields": "place_id",
            "key": self._api_key
        }
        search_response = requests.get(place_search_url, params=_search_params)
        place_data = search_response.json()
        place_id = None
        if "candidates" in place_data and place_data["candidates"]:
            place_id = place_data["candidates"][0]["place_id"]
        return place_id

    def _get_place_detail(self, place_id: str):
        rating = None
        list_reviews = []
        list_photos = []
        params = {
            "place_id": place_id,
            "fields": "rating,reviews,photos",
            "language": "es",
            "key": self._api_key
        }
        response = requests.get(place_details_url, params=params)
        place_details = response.json()
        if "result" in place_details:
            result = place_details["result"]
            rating = result.get("rating")
            if "reviews" in result:
                for review in result["reviews"][:5]:
                    list_reviews.append({
                        'author': review.get("author_name", "Anónimo"),
                        'text': review.get("text", ""),
                        'rating': review.get("rating")
                    })
            if "photos" in result:
                for photo in result["photos"][:3]:
                    photo_reference = photo["photo_reference"]
                    list_photos.append({
                        'reference': photo_reference,
                        'link': f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
                                f"{photo_reference}&key={self._api_key}"
                    })
        return {
            'rating': rating,
            'list_reviews': list_reviews,
            'list_photos': list_photos
        }
