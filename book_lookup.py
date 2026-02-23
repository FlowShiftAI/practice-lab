"""書籍番号から書籍名を返すシンプルなプログラム。"""

BOOK_CATALOG = {
    "001": "Python入門",
    "002": "実践データ分析",
    "003": "アルゴリズム図鑑",
    "004": "Web開発ハンドブック",
    "005": "機械学習スタートガイド",
}


def get_book_name(book_number: str) -> str:
    """書籍番号に対応する書籍名を返す。未登録の場合はメッセージを返す。"""
    return BOOK_CATALOG.get(book_number, "該当する書籍が見つかりません")


def main() -> None:
    book_number = input("書籍番号を入力してください: ").strip()
    print(f"書籍名: {get_book_name(book_number)}")


if __name__ == "__main__":
    main()
