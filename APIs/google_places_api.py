import requests

# AIzaSyAXL42QMkpSpFKCMtryyE27lcjOMBzm13I
def get_google_reviews(api_key, place_id):
    """
    Description:
    Fetches restaurant details and reviews from Google Places API for a given place_id.
    
    Parameters:
        api_key (str): Google Places API key.
        place_id (str): The unique identifier for the place you want reviews for.
        
    Returns:
        restaurant_info: A dictionary containing the restaurant name, rating, and a list of reviews.
        If the API call fails, it returns an empty dictionary.
    """
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,rating,reviews",
        "key": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
    except requests.RequestException as e:
        print(f"Error fetching data from Google Places API: {e}")
        return {}
    
    data = response.json()
    
    if data.get("status") != "OK":
        print(f"Google API returned error status: {data.get('status')}")
        return {}
    
    result = data.get("result", {})
    restaurant_info = {
        "name": result.get("name"),
        "rating": result.get("rating"),
        "reviews": []
    }
    
    reviews = result.get("reviews", [])
    for review in reviews:
        review_data = {
            "author": review.get("author_name"),
            "rating": review.get("rating"),
            "text": review.get("text"),
            "time": review.get("time")  
        }
        restaurant_info["reviews"].append(review_data)
    
    return restaurant_info  
    
    
if __name__ == "__main__":
    API_KEY = "AIzaSyAXL42QMkpSpFKCMtryyE27lcjOMBzm13I"
    PLACE_ID = "ChIJt8Q3HABhwokRc3FsBemPWAo" # replace with nearby search
    
    info = get_google_reviews(API_KEY, PLACE_ID)
    if info:
        print("Restaurant Name:", info.get("name"))
        print("Overall Rating:", info.get("rating"))
        print("Reviews:")
        for idx, review in enumerate(info.get("reviews"), start=1):
            print(f"{idx}. {review.get('author')}: {review.get('rating')} stars")
            print(f"   {review.get('text')}\n")
    else:
        print("No data returned from the API.")