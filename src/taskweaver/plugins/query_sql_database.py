from typing import Any, Dict

def query_sql_database(
    llm: BaseLanguageModel,
    db: SQLDatabase,
    question: str,
    table_names_to_use: Optional[List[str]] = None,
    k: int = 5
) -> str:
    """
    TaskWeaver plugin to query an SQL database.

    Args:
        llm: The language model to use.
        db: The SQLDatabase instance to generate the query for.
        question: The natural language question to convert into SQL.
        table_names_to_use: Optional list of table names to use in the query.
        k: The number of results per select statement to return.

    Returns:
        The SQL query generated from the natural language question.
    """
    sql_input = {"question": question}
    if table_names_to_use:
        sql_input["table_names_to_use"] = table_names_to_use

    # Create a chain that generates SQL queries
    sql_chain = create_sql_query_chain(llm, db, k=k)

    # Execute the chain and return the SQL query
    return sql_chain(sql_input)
