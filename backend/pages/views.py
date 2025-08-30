from django.http import JsonResponse

CONTENT = {
    "speaker-coaching": {
        "title": "Speaker Coaching - Uplevel public speaking",
        "body": (
            "Speaker Coaching for executives, leaders, subject matter experts, "
            "salespeople, and individual contributors the 1-on-1, personalized "
            "feedback and development training they need to move their audiences to action."
        ),
    },
    "sales-enablement": {
        "title": "Sales enablement consulting",
        "body": (
            "Equip sales teams with persuasive stories, pitches, presentations, and tools "
            "that create demand and drive conversions. With our sales enablement consulting, "
            "you can increase your revenue using key principles such as empathy, clarity, and story."
        ),
    },
    "technical-sales": {
        "title": "Technical Sales consulting",
        "body": (
            "Equip the most valuable members of your sales teams—the technical sales engineers—"
            "with persuasive stories, pitches, presentations, and tools that create demand and "
            "drive conversions. With our technical sales enablement consulting, you can increase "
            "your success rate using key principles such as empathy, clarity, and story."
        ),
    },
}


def page_content(request, slug):
    data = CONTENT.get(slug)
    if not data:
        return JsonResponse({"error": "Not found"}, status=404)
    return JsonResponse(data)
