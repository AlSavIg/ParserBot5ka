import datetime
import aiofiles
import requests
from aiocsv import AsyncWriter

items_on_page = 30
page = 1
selected_stores = {
    '33YU': 'Косыгина, 31',
    '5677': 'Наставников пр, 3',
    '5593': 'Садовая, 69 лит.А'
}


def parse_json_card(item):
    pass


def get_data_from_json(local_url):
    response = requests.get(url=local_url)
    data = response.json()
    data_container = []
    while data.get('next') is not None:
        local_url = data.get('next')
        results = data.get('results')
        for item in results:
            parsed_data = parse_json_card(item)
            data_container.append(parsed_data)
        response = requests.get(url=local_url)
        data = response.json()
    return data_container


async def collect_data(shop_id):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    url = 'https://5ka.ru/api/v2/special_offers/' \
          f'?records_per_page={items_on_page}' \
          f'&page={page}' \
          f'&store={shop_id}' \
          '&ordering=' \
          '&price_promo__gte=' \
          '&price_promo__lte=' \
          '&categories=' \
          '&search='

    data = get_data_from_json(local_url=url)

    async with aiofiles.open(f'{selected_stores[shop_id]}_{cur_time}.csv', 'w',
                             encoding='utf-8',
                             newline='') as file:
        writer = AsyncWriter(file)

        await writer.writerow(
            [
                'Наименование',
                'Ссылка_на_изображение',
                'Период_акции',
                'Старая_цена',
                'Новая_цена',
                'Скидка'
            ]
        )
        await writer.writerows(data)

    return f'{selected_stores[shop_id]}_{cur_time}.csv'
