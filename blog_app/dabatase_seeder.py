from core.models.post import Post
import random
from core.extensions import db
from core.models.question import Question
db.create_all()

for i in range(0, 10):
     random_num = random.randrange(1, 1000)
     post = Post(title=f'Post #{random_num}', content=f'Content #{random_num}')
     db.session.add(post)
     print(post)
     print(post.content)
     print('--')
     db.session.commit()

# Question model seeder

q1 = Question(content='Why is the sky blue?', answer='Because... Why not?')
q2 = Question(content='What is love?', answer='A portal to the underworld.')
db.session.add_all([q1, q2])
db.session.commit()

# Run this command to execute the seeder in flask shell:
# exec(open('dabatase_seeder.py').read())
