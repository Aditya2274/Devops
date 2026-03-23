import requests
def fetch_random_cat_fact():
    url="https://catfact.ninja/fact"

    try:
        response= requests.get(url)
        response.raise_for_status()
        fact=response.text
        return fact
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None
    
def main():
    fact=fetch_random_cat_fact()
    if fact:
        print("Random cat fact:")
        print(fact)

if __name__=="__main__":
    main()