from knowledge_base import identify_topic
from knowledge_base import get_article_content


def test_certification_question():
    result = identify_topic("How do I get certified?")
    assert result == "certification"


def test_analytics_question():
    result = identify_topic("Where can I see my completion rates?")
    assert result == "analytics"


def test_user_management_question():
    result = identify_topic("How do I add a learner?")
    assert result == "user_management"


def test_admin_can_access_analytics():
    result = get_article_content("analytics", "admin")
    assert isinstance(result, dict)


def test_learner_cannot_access_analytics():
    result = get_article_content("analytics", "learner")
    assert result == "You do not have permission to view this content."


def test_learner_can_access_certification():
    result = get_article_content("certification", "learner")
    assert isinstance(result, dict)
