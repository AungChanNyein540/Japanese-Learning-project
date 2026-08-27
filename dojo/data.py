# -*- coding: utf-8 -*-


HIRAGANA_ROWS = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", None, "ゆ", None, "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", None, None, None, "を"],
    ["ん", None, None, None, None],
]

HIRAGANA_ROMAJI = [
    ["a", "i", "u", "e", "o"],
    ["ka", "ki", "ku", "ke", "ko"],
    ["sa", "shi", "su", "se", "so"],
    ["ta", "chi", "tsu", "te", "to"],
    ["na", "ni", "nu", "ne", "no"],
    ["ha", "hi", "fu", "he", "ho"],
    ["ma", "mi", "mu", "me", "mo"],
    ["ya", None, "yu", None, "yo"],
    ["ra", "ri", "ru", "re", "ro"],
    ["wa", None, None, None, "wo"],
    ["n", None, None, None, None],
]

HIRAGANA_DAKUTEN_ROWS = [
    ["が", "ぎ", "ぐ", "げ", "ご"],
    ["ざ", "じ", "ず", "ぜ", "ぞ"],
    ["だ", "ぢ", "づ", "で", "ど"],
    ["ば", "び", "ぶ", "べ", "ぼ"],
    ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"],
]

HIRAGANA_DAKUTEN_ROMAJI = [
    ["ga", "gi", "gu", "ge", "go"],
    ["za", "ji", "zu", "ze", "zo"],
    ["da", "ji", "zu", "de", "do"],
    ["ba", "bi", "bu", "be", "bo"],
    ["pa", "pi", "pu", "pe", "po"],
]

KATAKANA_ROWS = [
    ["ア", "イ", "ウ", "エ", "オ"],
    ["カ", "キ", "ク", "ケ", "コ"],
    ["サ", "シ", "ス", "セ", "ソ"],
    ["タ", "チ", "ツ", "テ", "ト"],
    ["ナ", "ニ", "ヌ", "ネ", "ノ"],
    ["ハ", "ヒ", "フ", "ヘ", "ホ"],
    ["マ", "ミ", "ム", "メ", "モ"],
    ["ヤ", None, "ユ", None, "ヨ"],
    ["ラ", "リ", "ル", "レ", "ロ"],
    ["ワ", None, None, None, "ヲ"],
    ["ン", None, None, None, None],
]

KATAKANA_ROMAJI = HIRAGANA_ROMAJI  

KATAKANA_DAKUTEN_ROWS = [
    ["ガ", "ギ", "グ", "ゲ", "ゴ"],
    ["ザ", "ジ", "ズ", "ゼ", "ゾ"],
    ["ダ", "ヂ", "ヅ", "デ", "ド"],
    ["バ", "ビ", "ブ", "ベ", "ボ"],
    ["パ", "ピ", "プ", "ペ", "ポ"],
]

KATAKANA_DAKUTEN_ROMAJI = HIRAGANA_DAKUTEN_ROMAJI


def paired_grid(rows, romaji_rows):
   
    grid = []
    for r_idx, row in enumerate(rows):
        grid_row = []
        for c_idx, char in enumerate(row):
            if char:
                grid_row.append({"char": char, "romaji": romaji_rows[r_idx][c_idx]})
            else:
                grid_row.append(None)
        grid.append(grid_row)
    return grid


def flat_kana_pairs(rows, romaji_rows):
    """Flatten a kana grid into a list of {char, romaji} dicts, skipping gaps."""
    pairs = []
    for r_idx, row in enumerate(rows):
        for c_idx, char in enumerate(row):
            if char:
                pairs.append({"char": char, "romaji": romaji_rows[r_idx][c_idx]})
    return pairs


HIRAGANA_ALL = flat_kana_pairs(HIRAGANA_ROWS, HIRAGANA_ROMAJI) + flat_kana_pairs(
    HIRAGANA_DAKUTEN_ROWS, HIRAGANA_DAKUTEN_ROMAJI
)
KATAKANA_ALL = flat_kana_pairs(KATAKANA_ROWS, KATAKANA_ROMAJI) + flat_kana_pairs(
    KATAKANA_DAKUTEN_ROWS, KATAKANA_DAKUTEN_ROMAJI
)

# JLPT N5-level vocabulary, grouped by everyday category.
VOCABULARY = [
    # Greetings
    {"kanji": "おはよう", "reading": "おはよう", "romaji": "ohayou", "meaning": "good morning", "category": "Greetings"},
    {"kanji": "こんにちは", "reading": "こんにちは", "romaji": "konnichiwa", "meaning": "hello / good afternoon", "category": "Greetings"},
    {"kanji": "こんばんは", "reading": "こんばんは", "romaji": "konbanwa", "meaning": "good evening", "category": "Greetings"},
    {"kanji": "ありがとう", "reading": "ありがとう", "romaji": "arigatou", "meaning": "thank you", "category": "Greetings"},
    {"kanji": "すみません", "reading": "すみません", "romaji": "sumimasen", "meaning": "excuse me / sorry", "category": "Greetings"},
    {"kanji": "さようなら", "reading": "さようなら", "romaji": "sayounara", "meaning": "goodbye", "category": "Greetings"},
    # People & Family
    {"kanji": "私", "reading": "わたし", "romaji": "watashi", "meaning": "I / me", "category": "People"},
    {"kanji": "友達", "reading": "ともだち", "romaji": "tomodachi", "meaning": "friend", "category": "People"},
    {"kanji": "先生", "reading": "せんせい", "romaji": "sensei", "meaning": "teacher", "category": "People"},
    {"kanji": "学生", "reading": "がくせい", "romaji": "gakusei", "meaning": "student", "category": "People"},
    {"kanji": "家族", "reading": "かぞく", "romaji": "kazoku", "meaning": "family", "category": "People"},
    {"kanji": "母", "reading": "はは", "romaji": "haha", "meaning": "mother (own)", "category": "People"},
    {"kanji": "父", "reading": "ちち", "romaji": "chichi", "meaning": "father (own)", "category": "People"},
    # Food
    {"kanji": "水", "reading": "みず", "romaji": "mizu", "meaning": "water", "category": "Food"},
    {"kanji": "米", "reading": "こめ", "romaji": "kome", "meaning": "rice (uncooked)", "category": "Food"},
    {"kanji": "魚", "reading": "さかな", "romaji": "sakana", "meaning": "fish", "category": "Food"},
    {"kanji": "肉", "reading": "にく", "romaji": "niku", "meaning": "meat", "category": "Food"},
    {"kanji": "野菜", "reading": "やさい", "romaji": "yasai", "meaning": "vegetable", "category": "Food"},
    {"kanji": "果物", "reading": "くだもの", "romaji": "kudamono", "meaning": "fruit", "category": "Food"},
    {"kanji": "朝ご飯", "reading": "あさごはん", "romaji": "asagohan", "meaning": "breakfast", "category": "Food"},
    # Places
    {"kanji": "学校", "reading": "がっこう", "romaji": "gakkou", "meaning": "school", "category": "Places"},
    {"kanji": "家", "reading": "いえ", "romaji": "ie", "meaning": "house / home", "category": "Places"},
    {"kanji": "駅", "reading": "えき", "romaji": "eki", "meaning": "station", "category": "Places"},
    {"kanji": "病院", "reading": "びょういん", "romaji": "byouin", "meaning": "hospital", "category": "Places"},
    {"kanji": "図書館", "reading": "としょかん", "romaji": "toshokan", "meaning": "library", "category": "Places"},
    {"kanji": "会社", "reading": "かいしゃ", "romaji": "kaisha", "meaning": "company / office", "category": "Places"},
    # Time
    {"kanji": "今日", "reading": "きょう", "romaji": "kyou", "meaning": "today", "category": "Time"},
    {"kanji": "明日", "reading": "あした", "romaji": "ashita", "meaning": "tomorrow", "category": "Time"},
    {"kanji": "昨日", "reading": "きのう", "romaji": "kinou", "meaning": "yesterday", "category": "Time"},
    {"kanji": "今", "reading": "いま", "romaji": "ima", "meaning": "now", "category": "Time"},
    {"kanji": "毎日", "reading": "まいにち", "romaji": "mainichi", "meaning": "every day", "category": "Time"},
    {"kanji": "時間", "reading": "じかん", "romaji": "jikan", "meaning": "time / hour", "category": "Time"},
    # Verbs
    {"kanji": "食べる", "reading": "たべる", "romaji": "taberu", "meaning": "to eat", "category": "Verbs"},
    {"kanji": "飲む", "reading": "のむ", "romaji": "nomu", "meaning": "to drink", "category": "Verbs"},
    {"kanji": "見る", "reading": "みる", "romaji": "miru", "meaning": "to see / watch", "category": "Verbs"},
    {"kanji": "聞く", "reading": "きく", "romaji": "kiku", "meaning": "to listen / ask", "category": "Verbs"},
    {"kanji": "行く", "reading": "いく", "romaji": "iku", "meaning": "to go", "category": "Verbs"},
    {"kanji": "来る", "reading": "くる", "romaji": "kuru", "meaning": "to come", "category": "Verbs"},
    {"kanji": "読む", "reading": "よむ", "romaji": "yomu", "meaning": "to read", "category": "Verbs"},
    {"kanji": "書く", "reading": "かく", "romaji": "kaku", "meaning": "to write", "category": "Verbs"},
    {"kanji": "話す", "reading": "はなす", "romaji": "hanasu", "meaning": "to speak", "category": "Verbs"},
    {"kanji": "買う", "reading": "かう", "romaji": "kau", "meaning": "to buy", "category": "Verbs"},
    # Adjectives
    {"kanji": "大きい", "reading": "おおきい", "romaji": "ookii", "meaning": "big", "category": "Adjectives"},
    {"kanji": "小さい", "reading": "ちいさい", "romaji": "chiisai", "meaning": "small", "category": "Adjectives"},
    {"kanji": "新しい", "reading": "あたらしい", "romaji": "atarashii", "meaning": "new", "category": "Adjectives"},
    {"kanji": "古い", "reading": "ふるい", "romaji": "furui", "meaning": "old (things)", "category": "Adjectives"},
    {"kanji": "楽しい", "reading": "たのしい", "romaji": "tanoshii", "meaning": "fun / enjoyable", "category": "Adjectives"},
    {"kanji": "難しい", "reading": "むずかしい", "romaji": "muzukashii", "meaning": "difficult", "category": "Adjectives"},
    # Numbers
    {"kanji": "一", "reading": "いち", "romaji": "ichi", "meaning": "one", "category": "Numbers"},
    {"kanji": "二", "reading": "に", "romaji": "ni", "meaning": "two", "category": "Numbers"},
    {"kanji": "三", "reading": "さん", "romaji": "san", "meaning": "three", "category": "Numbers"},
    {"kanji": "四", "reading": "よん", "romaji": "yon", "meaning": "four", "category": "Numbers"},
    {"kanji": "五", "reading": "ご", "romaji": "go", "meaning": "five", "category": "Numbers"},
]

VOCAB_CATEGORIES = sorted(set(item["category"] for item in VOCABULARY))

