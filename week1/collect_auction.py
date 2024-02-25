import requests
from urllib import parse
from dotenv import load_dotenv
import os
import psycopg2

# .env 파일을 만들어서 사용합니다. 

load_dotenv()
apiKey = os.getenv("apiKey")
host = os.getenv("host")
db_name = os.getenv("db_name")
user = os.getenv("user")
password = os.getenv("password")


def search_item_info(item="50프로 +7 장비 강화권", search_num=50, apiKey=apiKey):
    encoded_item = parse.quote(item)
    itemid_serach_url = (
        f"https://api.neople.co.kr/df/items?itemName={encoded_item}&apikey={apiKey}"
    )

    res = requests.get(itemid_serach_url)
    result = res.json()["rows"]
    return result



def search_item_in_auction(item="50프로 +7 장비 강화권", apiKey=apiKey, search_num=50):
    encoded_item = parse.quote(item)

    item_search_in_auction_url = f"https://api.neople.co.kr/df/auction?itemName={encoded_item}&sort=unitPrice:asc&limit={search_num}&apikey={apiKey}"
    res = requests.get(item_search_in_auction_url)
    results = res.json()["rows"]
    return results



def save_results(results, host=host, db_name=db_name, user=user, password=password):

    conn = psycopg2.connect(
        host=host, dbname=db_name, user=user, password=password, port=5432
    )

    data = []

    for result in results:
        data.append(
            (
                result["itemName"],
                result["regDate"],
                result["expireDate"],
                result["count"],
                result["currentPrice"],
                result["unitPrice"],
            )
        )

    query = "INSERT INTO auction_items(item_name,regDate,expireDate,count,currentPrice,unitPrice) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor = conn.cursor()
    cursor.executemany(query, data)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":

    rows = search_item_in_auction()

    print(rows)
    save_results(rows)
    pass

    # collect_auction_item()
