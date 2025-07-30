def parse_ingredients(response_text):
    # 예: "보이는 채소: 표고버섯4, 파프리카1, 당근1, 애호박1, 가지1, 양배추1/4"
    if ":" not in response_text:
        return {}

    _, items_str = response_text.split(":", 1)
    items = items_str.split(",")

    result = {}
    for item in items:
        item = item.strip()
        # 숫자랑 단어 분리
        name = "".join(filter(str.isalpha, item))
        amount = item.replace(name, "").strip()
        result[name] = amount

    return result
