import requests


url = 'http://shopping.dangdang.com/shoppingcart/newShow?_=1615533012850'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'Cookie': 'ddscreen=2; from=460-5-biaoti; order_follow_source=P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.000000KsUNK1nh4-NOSxAYFGXeROR7wWB1ceGsXjhxP7xXB_Y2rx9Zt1nYh7QlWgqnaEUD6--%7C%230-%7C-; ddscreen=2; __permanent_id=20210312144215785927700316719929795; __visit_id=20210312144215789335395429545258514; __out_refer=1615531336%7C!%7Cwww.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593; __ddc_1d=1615531336%7C!%7C_utm_brand_id%3D11106; __ddc_24h=1615531336%7C!%7C_utm_brand_id%3D11106; __ddc_15d=1615531336%7C!%7C_utm_brand_id%3D11106; __ddc_15d_f=1615531336%7C!%7C_utm_brand_id%3D11106; cart_uuid=60192811340003; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D1%26district_id%3D101%26town_id%3D0; cart_items_count=1; _jzqco=%7C%7C%7C%7C%7C1.190519960.1615531342530.1615531342530.1615531342530.1615531342530.1615531342530.0.0.0.1.1; __rpm=p_29164456.030..1615531341977%7C...1615531346580; cart_id=3000601928113400037; __trace_id=20210312150644967261094410781259348; JSESSIONID=596C69479BECA49CBF5F21EEF4A7399F'
}


req = requests.get(url=url, headers=headers)

print(req.json())

# with open('danfdang.html', 'wb') as fp:
#     fp.write(req.content)