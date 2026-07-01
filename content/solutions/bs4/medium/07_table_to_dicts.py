from bs4 import BeautifulSoup

def table_rows(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
    result = []
    for row in rows[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all('td')]
        result.append(dict(zip(headers, cells)))
    return result
