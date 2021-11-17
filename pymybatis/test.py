import mybatis_mapper2sql
mapper, xml_raw_text = mybatis_mapper2sql.create_mapper(xml='./pymybatis/test.xml')
# statement = mybatis_mapper2sql.get_statement(mapper, result_type='raw', reindent=True, strip_comments=False)
# print(statement)
