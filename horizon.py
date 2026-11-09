# product_name = "Horizon"
# product_type = "Training and Certification Platform"
# assistant_name = "Nova"
# print("Welcome to", product_name)
# print("Your", product_type)
# print(f"Hi! I'm {assistant_name}, your Customer Education Assistant.")
# customer_name = input("What's your name? ")
# # print(f"Nice to meet you, {customer_name}!")
# # customer_role = input("Are you an admin, instructor, or a learner? ").lower().strip()
# # if customer_role == "admin":
# #     print("You have access to administrator tools!")
# # elif customer_role == "instructor":
# #     print("Welcome to your course management dashboard!")
# # elif customer_role == "learner":
# #     print("Welcome to your learning dashboard!")
# # else:
# #     print("Sorry, I don't recognize that role.")
# # # knowledge_base = {
# # #     "certification": "You can view your certifications on the Credentials page.",
# # #     "course": "You can view your assigned courses in the My Learning dashboard.",
# # #     "report": "You can access training reports from the administrator dashboard.",
# # #     "password": "You can reset your password from the login screen."
# # # }
# # # knowledge_base["password"] = "Password resets are availabnle from the Account Settings page."
# # # knowledge_base["course"] = "Assigned courses are now available on the Courses page."
# # # topic = input("Which knowledge base topic would you like to look up? ").lower().strip()
# # # print(knowledge_base.get(topic, "Sorry, that topic isn't in the knowledge base yet."))
# # # customer_question = input(f"What can I help you with today, {customer_name}? ").lower().strip()
# # # if "certification" in customer_question:
# # #     print(knowledge_base["certification"])
# # # elif "course" in customer_question:
# # #     print(knowledge_base["course"])
# # # elif "report" in customer_question:
# # #     if customer_role == "admin":
# # #         print(knowledge_base["report"])
# # #     else:
# # #         print("Training reports are only available to administrators.")
# # # else:
# # #     print("I'm sorry, I don't have information about that topic yet.")
# # # test_article = {
# # #     "title": "Resetting Your Password",
# # #     "content": "You can reset your password from the login screen.",
# # #     "access": "all"
# # # }
# # # course_article = {
# # #     "title": "Viewing Your Courses",
# # #     "content": "You can view your assigned courses in the My Learning dashboard.",
# # #     "access": "all"
# # # }
# # # test_knowledge_base = {
# # #     "password": test_article,
# # #     "course": course_article
# # # }
# # # print(test_knowledge_base["password"]["title"])
# # # print(test_knowledge_base["password"]["access"])
# # # print(test_knowledge_base["password"].get("author", "No author listed."))
# # # print(test_knowledge_base["course"]["content"])
# # # topic = input("Which topic would you like help with? ").lower().strip()
# # # article = test_knowledge_base.get(topic)
# # # if article:
# # #     print(article["title"])
# # #     print(article["content"])
# # # else: 
# # #     print("Sorry, I don't have an article about that topic yet.")
# practice_kb = {
#     "learning_path": {
#         "title": "Understanding Learning Paths",
#         "content": "Learning paths organize courses into structured learning experiences.",
#         "access": "all"
#     },
#     "analytics": {
#         "title": "Viewing Learning Analytics",
#         "content": "Administrators can view learning analytics from the reporting dashboard.",
#         "access": "admin"
#     }
# }
# topic = input("Which topic would you like help with? ").lower().strip()
# article = practice_kb.get(topic)
# if article: 
#     if article["access"] == "all" or article["access"] == customer_role:
#         print(article["title"])
#         print(article["content"])
#     else:
#         print("You do not have permission to view this article.")
# else:
#     print("No article available.")
# # def greet_learner(name):
# #     print(f"Welcome back, {name}!")
# # greet_learner(customer_name)
# # def recommend_course(course_name):
# #     return f"I recommend taking the {course_name} course."
# # recommendation = recommend_course("Getting Started")
# # print(recommendation)
# def get_article_content(topic, customer_role):
#     article = practice_kb.get(topic)
#     if article:
#         if article["access"] == "all" or article["access"] == customer_role:
#             return article["content"]
#         else:
#             return "You do not have permission to view this content."
#     else: 
#         return "No article available."
# print(get_article_content("learning_path", "learner"))
# print(get_article_content("analytics", "learner"))
# print(get_article_content("certification", "admin"))