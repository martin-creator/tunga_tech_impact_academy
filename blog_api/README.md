<!-- SQLAlchemy is the ORM library, that helps map Python classes to database tables and columns, and turns Python objects of those classes into specific rows.

Flask-SQLAlchemy is a Flask extension which helps connect SQLAlchemy to Flask apps. -->


# Blog APIs


# Run backgroud worker: 
```docker run -w /app blog-api sh -c "rq worker -u rediss://red-cnspldnjbltc73ev1840:26L3hyoCwib32115FC2L1qP5nRq2g49Y@oregon-redis.render.com:6379 emails"```

# Run app
```docker run -p 5000:5000 blog-api sh -c "flask run --host 0.0.0.0"```


rq worker -u rediss://red-cnspldnjbltc73ev1840:26L3hyoCwib32115FC2L1qP5nRq2g49Y@oregon-redis.render.com:6379 emails