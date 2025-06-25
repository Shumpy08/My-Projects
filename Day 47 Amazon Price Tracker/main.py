import smtplib

import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7"
}
response = requests.get(url=url, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
price = soup.find(name="span", class_="a-price-whole").getText()
floating_price = float(price)
print(floating_price)
product = soup.find(id="productTitle").getText().split(", ")[0]
print(product)

user_id = "codeniqqer08@gmail.com"
password = "csyvqyyuaxzeosma"

buy_price = 200
if floating_price < buy_price:
    message = f"{product} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user_id, password)
        connection.sendmail(
            from_addr=user_id,
            to_addrs="shumpy0808@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))
