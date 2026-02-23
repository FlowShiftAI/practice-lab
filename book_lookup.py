"""Open Library API経由でISBNから書籍情報を取得するCLI。"""

from __future__ import annotations

import argparse
import json
from urllib import error, parse, request

OPEN_LIBRARY_API = "https://openlibrary.org/api/books"
NOT_FOUND_MESSAGE = "該当する書籍が見つかりません"


def normalize_isbn(isbn: str) -> str:
    """ISBN入力値からハイフンと空白を除去する。"""
    return isbn.replace("-", "").replace(" ", "").strip()


def fetch_book_info_by_isbn(isbn: str) -> dict[str, str] | None:
    """Open Library APIからISBNに対応する書籍情報を取得する。"""
    query = parse.urlencode(
        {
            "bibkeys": f"ISBN:{isbn}",
            "format": "json",
            "jscmd": "data",
        }
    )
    api_url = f"{OPEN_LIBRARY_API}?{query}"

    try:
        with request.urlopen(api_url, timeout=10) as response:
            payload = json.load(response)
    except (error.HTTPError, error.URLError, TimeoutError):
        return None

    book_data = payload.get(f"ISBN:{isbn}")
    if not book_data:
        return None

    title = book_data.get("title", "タイトル不明")
    authors = ", ".join(author.get("name", "不明") for author in book_data.get("authors", []))
    publish_date = book_data.get("publish_date", "不明")

    return {
        "title": title,
        "authors": authors or "不明",
        "publish_date": publish_date,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Open Library APIからISBNを使って書籍情報を取得します。"
    )
    parser.add_argument("--isbn", help="検索するISBN番号（ハイフン可）")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_isbn = args.isbn if args.isbn else input("ISBN番号を入力してください: ")
    isbn = normalize_isbn(raw_isbn)

    if not isbn:
        print("ISBN番号を入力してください")
        return

    book_info = fetch_book_info_by_isbn(isbn)
    if not book_info:
        print(NOT_FOUND_MESSAGE)
        return

    print("書籍情報:")
    print(f"ISBN: {isbn}")
    print(f"タイトル: {book_info['title']}")
    print(f"著者: {book_info['authors']}")
    print(f"出版日: {book_info['publish_date']}")


if __name__ == "__main__":
    main()
