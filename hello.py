"""A simple Python program for practice-lab."""


def main() -> None:
    """Ask the user for their name and print a friendly greeting."""
    name = input("あなたの名前を入力してください: ").strip()

    if not name:
        print("Hello from practice-lab!")
        return

    print(f"こんにちは、{name}さん！ practice-labへようこそ。")


if __name__ == "__main__":
    main()
