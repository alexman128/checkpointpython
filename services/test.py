import databases

q = databases.Test()
q.connect()
q.setQuery("select * from Sales")
q.do_query()
q.format_results()
r = q.output_results()
print(f"Los resultados son: {r}")

