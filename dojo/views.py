import random

from django.shortcuts import render, redirect

from .data import (
    HIRAGANA_ROWS, HIRAGANA_ROMAJI, HIRAGANA_DAKUTEN_ROWS, HIRAGANA_DAKUTEN_ROMAJI,
    KATAKANA_ROWS, KATAKANA_ROMAJI, KATAKANA_DAKUTEN_ROWS, KATAKANA_DAKUTEN_ROMAJI,
    HIRAGANA_ALL, KATAKANA_ALL, VOCABULARY, VOCAB_CATEGORIES, paired_grid,
)


# ---------------------------------------------------------------- helpers --

def build_question(request, quiz_type: str):
   
    if quiz_type == "katakana":
        pool = KATAKANA_ALL
    elif quiz_type == "vocabulary":
        pool = VOCABULARY
    else:
        quiz_type = "hiragana"
        pool = HIRAGANA_ALL

    item = random.choice(pool)

    if quiz_type == "vocabulary":
        question_text = item["kanji"]
        correct = item["meaning"]
        distractor_pool = [p["meaning"] for p in pool if p["meaning"] != correct]
        question_extra = item.get("reading", "")
    else:
        question_text = item["char"]
        correct = item["romaji"]
        distractor_pool = [p["romaji"] for p in pool if p["romaji"] != correct]
        question_extra = ""

    distractors = random.sample(distractor_pool, k=min(3, len(distractor_pool)))
    choices = distractors + [correct]
    random.shuffle(choices)

    request.session["quiz_type"] = quiz_type
    request.session["correct_answer"] = correct
    request.session["question_text"] = question_text
    request.session["question_extra"] = question_extra

    return {
        "question_text": question_text,
        "question_extra": question_extra,
        "choices": choices,
        "quiz_type": quiz_type,
    }


# ------------------------------------------------------------------ views --

def index(request):
    context = {
        "hiragana_count": len(HIRAGANA_ALL),
        "katakana_count": len(KATAKANA_ALL),
        "vocab_count": len(VOCABULARY),
        "score": request.session.get("score", 0),
        "attempts": request.session.get("attempts", 0),
    }
    return render(request, "dojo/index.html", context)


def hiragana(request):
    context = {
        "title": "Hiragana",
        "subtitle": "ひらがな",
        "description": "The Basics of Reading Japanese Katakana.",
        "base_grid": paired_grid(HIRAGANA_ROWS, HIRAGANA_ROMAJI),
        "dakuten_grid": paired_grid(HIRAGANA_DAKUTEN_ROWS, HIRAGANA_DAKUTEN_ROMAJI),
        "quiz_type": "hiragana",
    }
    return render(request, "dojo/kana.html", context)


def katakana(request):
    context = {
        "title": "Katakana",
        "subtitle": "カタカナ",
        "description": "The Basics of Reading Japanese Katakana.",
        "base_grid": paired_grid(KATAKANA_ROWS, KATAKANA_ROMAJI),
        "dakuten_grid": paired_grid(KATAKANA_DAKUTEN_ROWS, KATAKANA_DAKUTEN_ROMAJI),
        "quiz_type": "katakana",
    }
    return render(request, "dojo/kana.html", context)


def vocabulary(request):
    active_category = request.GET.get("category", "All")
    if active_category != "All" and active_category in VOCAB_CATEGORIES:
        words = [w for w in VOCABULARY if w["category"] == active_category]
    else:
        active_category = "All"
        words = VOCABULARY
    context = {
        "words": words,
        "categories": ["All"] + VOCAB_CATEGORIES,
        "active_category": active_category,
    }
    return render(request, "dojo/vocabulary.html", context)


def quiz(request):
    quiz_type = request.GET.get("type", request.session.get("quiz_type", "hiragana"))
    if quiz_type not in ("hiragana", "katakana", "vocabulary"):
        quiz_type = "hiragana"
    question = build_question(request, quiz_type)
    context = {
        "question": question,
        "score": request.session.get("score", 0),
        "attempts": request.session.get("attempts", 0),
        "feedback": None,
    }
    return render(request, "dojo/quiz.html", context)


def quiz_answer(request):
    chosen = request.POST.get("choice", "")
    correct = request.session.get("correct_answer", "")
    quiz_type = request.session.get("quiz_type", "hiragana")

    request.session["attempts"] = request.session.get("attempts", 0) + 1
    is_correct = chosen == correct
    if is_correct:
        request.session["score"] = request.session.get("score", 0) + 1

    feedback = {
        "is_correct": is_correct,
        "chosen": chosen,
        "correct": correct,
        "question_text": request.session.get("question_text", ""),
        "question_extra": request.session.get("question_extra", ""),
    }
    next_question = build_question(request, quiz_type)
    context = {
        "question": next_question,
        "score": request.session.get("score", 0),
        "attempts": request.session.get("attempts", 0),
        "feedback": feedback,
    }
    return render(request, "dojo/quiz.html", context)


def quiz_reset(request):
    request.session["score"] = 0
    request.session["attempts"] = 0
    quiz_type = request.session.get("quiz_type", "hiragana")
    return redirect(f"/quiz/?type={quiz_type}")

