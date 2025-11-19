from sqlalchemy import text
from app.db.session import AsyncSessionLocal

async def db_analysis_tool(query_str: str) -> str:
    """
    Executes a read-only SQL query against the database and returns the result.
    Useful for counting items, checking data distribution, etc.
    
    Args:
        query_str: The SQL query to execute. MUST be a SELECT statement.
    """
    # Basic safety check
    if not query_str.strip().lower().startswith("select"):
        return "Error: Only SELECT statements are allowed."

    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(text(query_str))
            rows = result.fetchall()
            return str(rows)
        except Exception as e:
            return f"Database Error: {str(e)}"
