practice_kb = {
    "learning_path": {
        "title": "Understanding Learning Paths",
        "content": "Learning paths organize courses into structured learning experiences.",
        "access": "all",
    },
    "analytics": {
        "title": "Viewing Learning Analytics",
        "content": "Administrators can view learning analytics from the reporting dashboard.",
        "access": "admin",
    },
    "certification": {
        "title": "Earning Your Certification",
        "content": "Complete all required courses and pass the certification assessment to earn your certificate. You can view completed certifications from your learner dashboard.",
        "access": "all",
    },
    "enrollment": {
        "title": "Enrolling in a Course",
        "content": "Browse the course catalog, select a course, and click Enroll to add it to your learning dashboard.",
        "access": "all",
    },
    "user_management": {
        "title": "Managing Learner Accounts",
        "content": "Administrators can add, edit, and deactivate learner accounts from the User Management dashboard.",
        "access": "admin",
    },
}

topic_keywords = {
    "learning_path":{
        "learning path", 
        "training path", 
        "learning track",
    },
    "analytics": {
        "analytics",
        "report",
        "dashboard",
        "completion rate",
        "training metrics",
    },
    "certification": {
        "certification", 
        "certificate", 
        "certified", 
        "certify",
    },
    "enrollment": {
        "enroll",
        "course catalog",
        "sign up",
        "register for a course",
        "join a course",
    },
    "user_management": {
        "user management",
        "learner account",
        "manage users",
        "add a learner",
        "deactivate account",
    }
}


def get_article_content(topic, customer_role):
    article = practice_kb.get(topic)

    if not article:
        return "No article available."

    if article["access"] == "all" or article["access"] == customer_role:
        return article
        
    return "You do not have permission to view this content."

def identify_topic(question):
    question = question.lower().strip()

    for topic, keywords in topic_keywords.items():
        if any(word in question for word in keywords):
            return topic
   
    return None
