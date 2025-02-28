df_parsed.writeStream \
    .outputMode("append") \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/mydb") \
    .option("dbtable", "student_marks") \
    .option("user", "username") \
    .option("password", "password") \
    .start()

